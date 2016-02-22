from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'cs'
        self.mark = '[CS]'
        self.filetypes = ['cs']
        self.input_pattern = '\.'
        self.is_bytepos = True

    def gather_candidates(self, context):
        return [dict(word='asdf', abbr='a', info='asdf', dup=1)]

