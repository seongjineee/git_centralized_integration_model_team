def calculator():
        try:
            expression = input("수식을 입력하세요: ")
            result = eval(expression)
            print(f"결과: {expression} = {result}")
        except:
                print("잘못된 수식입니다.")

while True:
    print("-------------------------")
    print("계산기 프로그램 메뉴")
    print("1: 사용\n2: 종료")
    print("-------------------------")
    choice = int(input("번호를 선택해주세요: "))

    if choice == 1:
        calculator()
    
    elif choice == 2:
        print("-------------------------")
        print("계산기를 종료합니다.")
        break

    elif choice != 1 and choice != 2:
        print("-------------------------")
        print("잘못된 선택입니다. 다시 시도해주세요.")