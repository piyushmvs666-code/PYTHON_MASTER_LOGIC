class Student:
    def _init_(self, name, student_id):
        self.name = name 
        self.student_id = student_id 
        self.eng_quiz = [] 
        self.math_quiz = [] 
        self.science_quiz = [] 

    def _str_(self):
        return f"Name: {self.name}, ID: {self.student_id}, Eng: {self.eng_quiz}, Math: {self.math_quiz}, Science: {self.science_quiz}"

    def set_eng_quiz(self, scores):
        self.eng_quiz = scores

    def set_math_quiz(self, scores):
        self.math_quiz = scores

    def set_science_quiz(self, scores):
        self.science_quiz = scores

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_eng_quiz(self):
        return self.eng_quiz

    def get_math_quiz(self):
        return self.math_quiz

    def get_science_quiz(self):
        return self.science_quiz

    def get_total_score(self):
        total = sum(self.eng_quiz) + sum(self.math_quiz) + sum(self.science_quiz)
        return total

    def get_avg_score(self):
        all_scores = self.eng_quiz + self.math_quiz + self.science_quiz
        if len(all_scores) == 0:
            return 0
        return sum(all_scores) / len(all_scores)
