import random
import unidecode
class UserChecking:
    def __init__(self, list_info): # [năm sinh, quê quan, cau hoi bao mat1, dap an1, cauhoi2, dapan2, cauhoi3, dapan3]
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
        self.fakeprovince = random.choice(self.province_check)
        if self.fakeprovince == list_info[0]: # creat anwser for yes no question
            self.list_info[0] = "chinh xac"
        else:
            self.list_info[0] = "khong dung"

        #self.fakeborn = str( list_info[0] + random.randint(-3, 3))
        # if self.fakeborn == list_info[0]: # creat anwser for yes no question
        #     self.list_info[0] = "đúng"
        # else:
        #     self.list_info[0] = "sai"
        # type =1: yes no question, type =0  ling quest
        self.fences = [
            # {
            #     'question' : "Bạn sinh năm:  " +  self.fakeborn,
            #     'anwser'   : self.list_info.pop(0),
            #     'type'     : 1,
            # },
            {
                'question' : "Quê bạn ở " + self.fakeprovince,
                'anwser'   : self.list_info.pop(0).lower(),
                'type'     : 1,
            },
            # 3 câu hỏi bảo mật
            {
                'question' : self.list_info.pop(0).lower(),
                'anwser'   : self.list_info.pop(0).lower(),
                'type'     : 0,
            },
            {
                'question': self.list_info.pop(0).lower(),
                'anwser':   self.list_info.pop(0).lower(),
                'type'   : 0,
            },
            {
                'question': self.list_info.pop(0).lower(),
                'anwser':   self.list_info.pop(0).lower(),
                'type' : 0
            },

        ]
        # chọn fence
        self.chosen_fence = random.choice(self.fences)

    def check(self, text):
        if self.chosen_fence['type'] == 1:  # yes no question
            if (text == self.chosen_fence['anwser'] and self.chosen_fence['anwser'] == 'đúng') or (text == self.chosen_fence['anwser'] and self.chosen_fence['anwser'] == 'sai'):
                return 1
            elif (text != self.chosen_fence['anwser'] and self.chosen_fence['anwser'] == 'đúng')  or (text != self.chosen_fence['anwser'] and self.chosen_fence['anwser'] == 'sai'):
                return 0
            else:
                return -1
        else:
            if text == self.chosen_fence['anwser']:
                return 1
            else:
                return 0
    def checkk(self, text):
        text = set(list(unidecode.unidecode(text.lower())))
        ref_text = set(list(unidecode.unidecode(self.chosen_fence['anwser'])))
        check = self.jaccard_similarity(text, ref_text)
        return check

    def jaccard_similarity(self, set1, set2):
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        similarity = intersection / union if union != 0 else 0  # Tránh chia cho 0
        return similarity

#list_infor = []
# person1 = UserChecking(list_info = [2002,"Thái Bình", "q1", "a1", "q2", "a2", "q3", "a3"])
# #person2 = UserChecking(list_info = [2003,"Hà Nội", "q1", "a1", "q2", "a2", "q3", "a3"])
#
# print(person1.check('đúng'))
# print(person1.chosen_fence)