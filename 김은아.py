# def exampleOne(a):
#     if not isinstance(a, int):
#         raise ValueError('정수를 입력해야 합니다.')
#     return a


def exampleone(a):
    # isinstance 자료형 확인 메서드, int나 float가 아니면
    if not isinstance(a, int) and not isinstance(a, float):

        # raise 예외 처리 메서드, JS의 throw와 같은 것
        raise ValueError('정수를 입력해야 합니다.')
        # 소수점일 경우 에러
    if a - int(a) != 0:
        raise ValueError('정수를 입력해야 합니다.')
    
    
    return a

print(exampleone(12))
