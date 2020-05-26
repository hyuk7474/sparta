name = 'bob'  # let 없고 ; 없고 주석은 #
num = 12 #똑같음
is_number = True # js에서는 true (대소문자 주의)

a_list = [] # 빈 리스트
a_list.append(1) # js에서는 push
a_list[0] # 호출하는 것은 똑같음
print(a_list)

a_dict = {}
a_dict = {'name' : 'bob', 'age' : 21}
a_dict['height'] = 178 # 새로 추가
print(a_dict['name']) # 값 가져오기
print(a_dict)

people = [{'name' : 'bob', 'age' : 24}, {'name' : 'je', 'age' : 31}]
print(people[0]['age'])