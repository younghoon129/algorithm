# 10 43
import itertools
import sys
sys.stdin = open("C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\1_A형\\250825_SWEA4128_요리사\\4128_input.txt", "r")

test = int(input())

for t in range(1, test+1):
    ingredients = int(input())
    ingredients_combo = [list(map(int, input().split())) for _ in range(ingredients)]
    ingredients_list = set([i for i in range(ingredients)]) # 조합 인덱스 번호표
    combo_list = list(itertools.combinations(ingredients_list, ingredients//2))  # 인덱스로 조합 계산

    gap_combo = -1
    for combo in combo_list:  # 각 조합별 계산
        other_combo = tuple(ingredients_list - set(combo))  # 나머지 인덱스 번호
        combo_cal = list(itertools.permutations(combo, 2))  # 점수 계산을 위해 2개씩 묶어 순열 생성
        other_combo_cal = list(itertools.permutations(other_combo, 2))  # 반대 점수 계산을 위해 2개씩 묶어 순열 생성

        combo_sum = 0
        other_combo_sum = 0
        cla_gap = 0
        for idx in range(len(combo_cal)):
            combo_sum += ingredients_combo[combo_cal[idx][0]][combo_cal[idx][1]]  # 점수 계산
            other_combo_sum += ingredients_combo[other_combo_cal[idx][0]][other_combo_cal[idx][1]]  # 반대 점수 계산
            cal_gap = abs(combo_sum - other_combo_sum)

        if gap_combo < 0:
            gap_combo = cal_gap
        else:
            gap_combo = min(gap_combo, cal_gap)
    
    print(f"#{t} {combo_list}")
