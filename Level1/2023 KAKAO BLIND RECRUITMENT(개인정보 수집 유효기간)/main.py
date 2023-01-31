def delete_calculate(dic_value, today, p_term):

    # 유효기간에 약관기간 더해주기
    p_term[1] = int(p_term[1]) + int(dic_value)
    Year = p_term[1]/12
    Year = int(Year)
    if not Year==0:
        print(Year)
        p_term[1] = int(p_term[1]%12)
        print(p_term[1])
        p_term[0] = int(p_term[0]) + Year
        if p_term[1]==0:
            p_term[1] = 12
            p_term[0] = p_term[0]-1

    print("today:",today)
    print("유효기간:",p_term)
    print("\n")


    # 유효기간과 오늘날짜 하나씩 비교해서 삭제
    if int(p_term[0]) > int(today[0]):
        return 0
    elif int(p_term[0]) < int(today[0]):
        return 1
    else:
        if int(p_term[1]) > int(today[1]):
            return 0
        elif int(p_term[1]) < int(today[1]):
            return 1
        else:
            if int(p_term[2]) > int(today[2]):
                return 0
            else:
                return 1


def solution(today, terms, privacies):  # 오늘 날짜, 유효기간, 개인정보 수집 일자
    # n개의 개인정보, 각각 유효기간 끝나면 파기해야함
    # today = yyyy.mm.dd
    # terms = ["A 6", "B 12", "C 3"] 각 달은 28일,
    # privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

    today = today.split(".")

    terms_dic = {terms[0].split(" ")[0]: int(terms[0].split(" ")[1])}

    for i in range(len(terms)):  # 약관 종류 dic 생성
        if not i == 0:
            terms_dic[terms[i].split(" ")[0]] = int(terms[i].split(" ")[1])

    privacies_list = []
    for i in range(len(privacies)):  # 개인정보 리스트 생성 for문
        temp = privacies[i].split(" ")
        privacies_list.append(temp)

    answer = []  # 파기해야할 개인정보 번호 : 오름차순으로 return 하도록

    for i in range(len(privacies_list)):  # 개인정보 처리 for문
        p_term = privacies_list[i][0].split(".")
        p_kind = privacies_list[i][1]
        dic_value = terms_dic[p_kind]
        if delete_calculate(dic_value, today, p_term) == 1:
            answer.append(i + 1)

    answer.sort(reverse=False)

    return answer



if __name__ == '__main__':
    today = "2022.05.19"
    terms = ["A 6", "B 18", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

    print(solution(today, terms, privacies))
