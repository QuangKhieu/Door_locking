import random
# questions = [
#     {
#         "question": "Câu hỏi số 1?",
#         "answers": ["A. Lựa chọn 1", "B. Lựa chọn 2", "C. Lựa chọn 3", "D. Lựa chọn 4"],
#         "correct_answer": "C"
#     },
#     {
#         "question": "Câu hỏi số 2?",
#         "answers": ["A. Lựa chọn 1", "B. Lựa chọn 2", "C. Lựa chọn 3", "D. Lựa chọn 4"],
#         "correct_answer": "A"
#     },
#     # Thêm các câu hỏi khác ở đây
#     ]
# # for question in questions:
# #     question["question"]  += 'abcd'
# #     print(question['question'])
# a = [2, "Quang", 20021571, "Nam", "Chó yêu thích:", "Shiba"]
# b = a.pop()
# b = a.pop()
# 
# print(a)

# list_info = [20,"Thái Bình", "q1", "a1", "q2", "a2", "q3", "a3"]
# province_check = [
# "Hà Nội",
# "Hồ Chí Minh",
# "Hải Phòng",
# "Đà Nẵng",
# "Cần Thơ",
# "An Giang",
# "Bà Rịa - Vũng Tàu",
# "Bạc Liêu",
# "Bắc Kạn",
# "Bắc Giang",
# "Bắc Ninh",
# "Bến Tre",
# "Bình Dương",
# "Bình Phước",
# "Bình Thuận",
# "Cà Mau",
# "Cao Bằng",
# "Đắk Lắk",
# "Đắk Nông",
# "Điện Biên",
# "Đồng Nai",
# "Đồng Tháp",
# "Gia Lai",
# "Hà Giang",
# "Hà Nam",
# "Hà Tĩnh",
# "Hải Dương",
# "Hậu Giang",
# "Hòa Bình",
# "Hưng Yên",
# "Khánh Hòa",
# "Kiên Giang",
# "Kon Tum",
# "Lai Châu",
# "Lâm Đồng",
# "Lạng Sơn",
# "Lào Cai",
# "Long An",
# "Nam Định",
# "Nghệ An",
# "Ninh Bình",
# "Ninh Thuận",
# "Phú Thọ",
# "Phú Yên",
# "Quảng Bình",
# "Quảng Nam",
# "Quảng Ngãi",
# "Quảng Ninh",
# "Quảng Trị",
# "Sóc Trăng",
# "Sơn La",
# "Tây Ninh",
# "Thái Bình",
# "Thái Nguyên",
# "Thanh Hóa",
# "Thừa Thiên-Huế",
# "Tiền Giang",
# "Trà Vinh",
# "Tuyên Quang",
# "Vĩnh Long",
# "Vĩnh Phúc",
# "Yên Bái",
# ]
# questions = [
#     {
#         'question' : "Tuổi của bạn là ",
#         'anwser'   : list_info.pop(0)
#     },
#     {
#         'question' : "Quê bạn ở " + random.choice(province_check),
#         'anwser'   : list_info.pop(0)
#     },
#     # 3 câu hỏi bảo mật
#     {
#         'question' : list_info.pop(0),
#         'anwser'   : list_info.pop(0)
#     },
#     {
#         'question': list_info.pop(0),
#         'anwser':   list_info.pop(0)
#     },
#     {
#         'question': list_info.pop(0),
#         'anwser':   list_info.pop(0)
#     },
#
# ]
# age_check = 0
# print(questions)
class UserChecking:
    def __init__(self, list_info):
        self.list_info = list_info
        self.list_info = list_info
        self.province_check = [
            "Hà Nội",
            "Hồ Chí Minh",
            "Hải Phòng",
            "Đà Nẵng",
            "Cần Thơ",
            "An Giang",
            "Bà Rịa - Vũng Tàu",
            "Bạc Liêu",
            "Bắc Kạn",
            "Bắc Giang",
            "Bắc Ninh",
            "Bến Tre",
            "Bình Dương",
            "Bình Phước",
            "Bình Thuận",
            "Cà Mau",
            "Cao Bằng",
            "Đắk Lắk",
            "Đắk Nông",
            "Điện Biên",
            "Đồng Nai",
            "Đồng Tháp",
            "Gia Lai",
            "Hà Giang",
            "Hà Nam",
            "Hà Tĩnh",
            "Hải Dương",
            "Hậu Giang",
            "Hòa Bình",
            "Hưng Yên",
            "Khánh Hòa",
            "Kiên Giang",
            "Kon Tum",
            "Lai Châu",
            "Lâm Đồng",
            "Lạng Sơn",
            "Lào Cai",
            "Long An",
            "Nam Định",
            "Nghệ An",
            "Ninh Bình",
            "Ninh Thuận",
            "Phú Thọ",
            "Phú Yên",
            "Quảng Bình",
            "Quảng Nam",
            "Quảng Ngãi",
            "Quảng Ninh",
            "Quảng Trị",
            "Sóc Trăng",
            "Sơn La",
            "Tây Ninh",
            "Thái Bình",
            "Thái Nguyên",
            "Thanh Hóa",
            "Thừa Thiên-Huế",
            "Tiền Giang",
            "Trà Vinh",
            "Tuyên Quang",
            "Vĩnh Long",
            "Vĩnh Phúc",
            "Yên Bái",
        ]
        self.questions = [
            {
                'question' : "Tuổi của bạn là ",
                'anwser'   : self.list_info.pop(0)
            },
            {
                'question' : "Quê bạn ở " + random.choice(self.province_check),
                'anwser'   : self.list_info.pop(0)
            },
            # 3 câu hỏi bảo mật
            {
                'question' : self.list_info.pop(0),
                'anwser'   : self.list_info.pop(0)
            },
            {
                'question': self.list_info.pop(0),
                'anwser':   self.list_info.pop(0)
            },
            {
                'question': self.list_info.pop(0),
                'anwser':   self.list_info.pop(0)
            },

        ]

# Tạo một đối tượng Person
person1 = UserChecking(list_info = [20,"Thái Bình", "q1", "a1", "q2", "a2", "q3", "a3"])
person2 = UserChecking(list_info = [20,"Thái Bình", "q1", "a1", "q2", "a2", "q3", "a3"])


print(person2.questions)

