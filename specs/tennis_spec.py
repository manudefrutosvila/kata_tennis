from expects import expect, be

class Scores(object):

    def __init__(self):
        self.values = [0, 15, 30, 40, 'A', 'W']
        self.current_score = 0

    def win_point(self):
        ++self.current_score

    def get_current_score(self):
         return self.values[self.current_score]


with description('Scores'):
    with before.each:
        self.scores = Scores()

    with it('should be 0 when it starts'):
        expect(self.scores.get_current_score()).to(be(0))

