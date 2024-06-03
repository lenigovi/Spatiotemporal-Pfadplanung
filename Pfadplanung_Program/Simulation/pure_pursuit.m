function [u, debug_info] = pure_pursuit(state, t, ref, param)
    % 
    % state = [x, y, qx, qy, qz, qw, delta]
    % u = [v_des, delta_des]
    % ref = [x_ref; y_ref; qx_ref; qy_ref; qz_ref; qw_ref; v_ref];
    % 
    
    IDX_X = 1;
    IDX_Y = 2;
    IDX_QUAT = 3:6;
    IDX_XY = 1:2;
    IDX_VEL = 7;
    
    lookahead_dist = param.pure_pursuit_lookahead;
    
    distance = vecnorm(ref(:,IDX_XY)' - state(IDX_XY)');
    [~, min_index] = min(distance);
    pr = ref(min_index, :);
    
    v_des = pr(IDX_VEL);
    
    for i = min_index:length(ref)
        dist = norm(ref(i, IDX_XY) - state(IDX_XY));
        if dist > lookahead_dist
            break;
        end
    end
    lookahead_pt = ref(i, :);
    
    state_dir = quat_to_dir(state(IDX_QUAT));
    lookahead_dir = lookahead_pt(IDX_XY) - state(IDX_XY);
    lookahead_dir = lookahead_dir / norm(lookahead_dir);
    
    % steering angle alpha
    alpha = atan2(lookahead_dir(2), lookahead_dir(1)) - atan2(state_dir(2), state_dir(1));
    
    omega_des = 2 * v_des * sin(alpha) / param.wheelbase;
    delta_des = atan2(omega_des * param.wheelbase, v_des);
    
    u = [v_des, delta_des];
    
    % Latitude error calc for debug
    pr_quat = pr(IDX_QUAT);
    sp_dir = quat_to_dir(pr_quat);
    T_xy2lonlat = [sp_dir(1), sp_dir(2); -sp_dir(2), sp_dir(1)];
    error_xy = (state(IDX_XY) - pr(IDX_XY))';
    error_lonlat = T_xy2lonlat * error_xy;
    error_lat = error_lonlat(2);
    
    debug_info = [lookahead_pt(IDX_X), lookahead_pt(IDX_Y), error_lat];
    
    end
    
    function dir = quat_to_dir(q)
        angle = atan2(2 * (q(4) * q(3) + q(1) * q(2)), 1 - 2 * (q(2)^2 + q(3)^2));
        dir = [cos(angle), sin(angle)];
    end
    