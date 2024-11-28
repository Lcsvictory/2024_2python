


class UserInfo:
    def __init__(self, uid:str, sex:str, height:float, weight:float):
        self.uid = uid
        self.sex = sex
        self.height = height
        self.weight = weight

    def cal_bmi(self):
        return f"{self.weight / (self.height *  self.height):.2f}"

    def save(self):
        return f"{self.uid}|{self.sex}|{self.height}|{self.weight}"
