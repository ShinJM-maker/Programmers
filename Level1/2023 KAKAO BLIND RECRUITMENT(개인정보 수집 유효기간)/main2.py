def delete_calculate(dic_value, today, p_term):
    if int(today[0]) * 12 * 28 + int(today[1]) * 28 + int(today[2]) >= int(p_term[0]) * 12 * 28 + int(p_term[1]) * 28 + int(p_term[2]) + int(dic_value) * 28:
        return 1

def solution(today, terms, privacies):  # 오늘 날짜, 유효기간, 개인정보 수집 일자
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
    return answer



if __name__ == '__main__':
    today = "2022.05.19"
    terms = ["A 6", "B 18", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

    print(solution(today, terms, privacies))

