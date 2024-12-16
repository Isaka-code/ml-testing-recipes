class Config:
    @classmethod
    def load(cls, path):
        # 実際はYAMLやJSONをロードする処理を入れる
        c = cls()
        c.learning_rate = 0.01
        return c
