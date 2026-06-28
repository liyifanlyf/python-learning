import math

def reward_function(params):
    """
    模型优化比赛 - 极简稳定版 (Final Optimized)
    核心策略：
    1. 硬边界保护：彻底杜绝冲出赛道。
    2. 线性速度分区：急弯慢、直道狠，逻辑清晰。
    3. 轻量级平滑：抑制“之”字形，提升效率。
    """

    # ==========================================
    # 1. 参数读取
    # ==========================================
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering_angle = params['steering_angle']
    closest_waypoints = params['closest_waypoints']

    # ==========================================
    # 2. 安全底线（绝对红线）
    # ==========================================
    # 只要掉下赛道，直接判死刑
    if not all_wheels_on_track:
        return 1e-4

    # ==========================================
    # 3. 居中奖励 (Center Reward)
    # ==========================================
    # 使用线性衰减，越靠近中心分数越高
    # 当距离 > 赛道宽度的 90% 时，奖励归零
    track_half_width = track_width / 2.0
    distance_ratio = distance_from_center / track_half_width
    
    # 如果离边缘太近 (超过90%)，直接重罚
    if distance_ratio > 0.9:
        return 1e-3
        
    center_reward = 1.0 - distance_ratio

    # ==========================================
    # 4. 转向平滑 (Anti-Zigzag)
    # ==========================================
    # 惩罚大幅度转向，鼓励平稳驾驶
    abs_steering = abs(steering_angle)
    
    # 转向越大，奖励倍率越低
    if abs_steering > 20:
        steering_factor = 0.5  # 急转弯打折
    elif abs_steering > 10:
        steering_factor = 0.8  # 缓转弯轻微打折
    else:
        steering_factor = 1.0  # 直行满分

    # ==========================================
    # 5. 动态速度控制 (Speed Control)
    # ==========================================
    # 获取当前位置
    next_point_idx = closest_waypoints[1]
    
    # 地形分区 (基于您的赛道图片)
    is_straight = (14 <= next_point_idx <= 61) or (next_point_idx >= 107)
    is_sharp_turn = (80 <= next_point_idx <= 106)
    is_medium_turn = (62 <= next_point_idx <= 79) or (1 <= next_point_idx <= 14)

    # 分段奖励
    if is_straight:
        # 直道：速度越快越好，最高2.5
        speed_reward = speed / 2.5
        
    elif is_sharp_turn:
        # 急弯：目标 1.0。高于1.0惩罚，低于1.0奖励减半
        if speed > 1.2:
            speed_reward = 0.2
        else:
            speed_reward = 0.8
            
    elif is_medium_turn:
        # 缓弯：目标 1.8
        if speed > 2.0:
            speed_reward = 0.5
        else:
            speed_reward = speed / 2.0
            
    else:
        speed_reward = speed / 2.5

    # ==========================================
    # 6. 最终加权计算
    # ==========================================
    # 权重分配：速度(50%) > 居中(40%) > 平滑(10%)
    total_reward = (
        speed_reward * 0.5 +
        center_reward * 0.4 +
        steering_factor * 0.1
    )

    return float(max(total_reward, 1e-3))