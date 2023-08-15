import sys

def main():
    T = int(sys.stdin.readline().rstrip())  # 테스트케이스 개수를 입력받음

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().rstrip().split())  # 두 정수 A와 B를 입력받음
        result = A + B
        print(result)  # A와 B를 더한 결과를 출력함

if __name__ == "__main__":
    main()