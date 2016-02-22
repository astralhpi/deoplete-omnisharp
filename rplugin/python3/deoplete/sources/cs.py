from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'cs'
        self.mark = '[CS]'
        self.filetypes = ['cs']
        self.input_pattern = '\.'
        self.is_bytepos = True

    def get_complete_position(self, context):
        print('asdf')
        return self.vim.call('OmniSharp#Complete', 1, 0)

    def gather_candidates(self, context):
        return self.vim.call('OmniSharp#Complete', 0, 0)

