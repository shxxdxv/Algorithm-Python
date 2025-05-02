def solution(sizes):
    
    width_max, height_max = 0, 0
    
    for width, height in sizes:
        # 세로가 가로보다 길다면 눕힘(swap으로 가로 세로 길이 변경)
        if width > height :
            width, height = height, width
        
        width_max = max(width_max, width)
        height_max = max(height_max, height)
    
    return width_max * height_max