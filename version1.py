# Функция ниже, чтобы избежать ошибку TypeError: can't send non-None value to a just-started generator
def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class LL:
    def __init__(self):
        """Инициализация"""
        self.stack = []
        self.stopped = False
        self.start = "E"
        self.stack.append(self.start)
        self.end_symbol = ""
        self.term = ''
        self.current_state = self.E()
        self.dict_state = {
            "E": self.E,
            "E_": self.E_,
            "T": self.T,
            "T_": self.T_,
            "F": self.F
        }

    def send(self, state):
        """Функция отправляет текущий ввод в current_state. В случае ошибки
        она захватывает исключение StopIteration и помечает флаг stopped."""
        try:
            self.current_state.send(state)
        except StopIteration:
            self.current_state = self.dict_state[self.stack[-1]]()
            self.stopped = True
        print(self.stack)

    def does_match(self):
        """Функция в любой момент времени возвращает True, если
        текущее состояние соответствует заданному конечному состоянию.
        Она также проверяет наличие флага stopped, который назначается,
        при неправильном вводе и дальнейшея итерация конечного автомата
        должна была быть остановлена."""
        if self.stopped:
            return False
        return self.stack[-1] == []

    @prime
    def E(self):
        while True:
            self.term = yield

            if self.term == "(":
                self.stack.pop(-1)
                self.stack.append("E_")
                self.stack.append("T")
                print(self.stack)
                #self.current_state = self.T()
                #self.term = yield
                self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "a":
                self.stack.pop(-1)
                self.stack.append("E_")
                self.stack.append("T")
                print(self.stack)
                #self.current_state = self.T()
                #self.term = yield
                self.current_state = self.dict_state[self.stack[-1]]()
            #self.term = yield
            else: break

    @prime
    def E_(self):
        while True:
            self.term = yield
            if self.term == ")":
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "+":
                self.stack.pop(-1)
                self.stack.append("E_")
                self.stack.append("T")
                self.stack.append("+")
                print(self.stack)
                # Добавить код #
                self.stack.pop(-1)
                print(self.stack)
                self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "-":
                self.stack.pop(-1)
                self.stack.append("E_")
                self.stack.append("T")
                self.stack.append("-")
                print(self.stack)
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                # Добавить код #
                self.current_state = self.T()
            elif self.term == "#":
                self.stack.pop(-1)
                #self.term = yield
                if self.stack == []:
                    print("стек опусташен")
                else:
                    self.current_state = self.dict_state[self.stack[-1]]()
            #self.term = yield
            else: break

    @prime
    def T(self):
        while True:
            #self.term = yield
            if self.term == "(":
                self.stack.pop(-1)
                self.stack.append("T_")
                self.stack.append("F")
                print(self.stack)
                self.term = yield
                self.current_state = self.F()
            elif s
elf.term == "a":
                self.stack.pop(-1)
                self.stack.append("T_")
                self.stack.append("F")
                print(self.stack)
                self.term = yield
                self.current_state = self.F()
            #self.term = yield
            else: break

    @prime
    def T_(self):
        while True:
            self.term = yield
            if self.term == ")":
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "+":
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "-":
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "*":
                self.stack.pop(-1)
                self.stack.append("T_")
                self.stack.append("F")
                self.stack.append("*")
                print(self.stack)
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                #self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "/":
                self.stack.pop(-1)
                self.stack.append("T_")
                self.stack.append("F")
                self.stack.append("/")
                print(self.stack)
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                #self.current_state = self.dict_state[self.stack[-1]]()
                #self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "#":
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                if self.stack == []:
                    print("стек опусташен")
                else:
                    self.current_state = self.dict_state[self.stack[-1]]()
            else:break


    @prime
    def F(self):
        while True:
            self.term = yield
            if self.term == "(":
                self.stack.pop(-1)
                self.stack.append(")")
                self.stack.append("E")
                self.stack.append("(")
                print(self.stack)
                self.stack.pop(-1)
                print(self.stack)
                self.current_state = self.E()
                #self.term = yield
                #self.current_state = self.dict_state[self.stack[-1]]()
            elif self.term == "a":
                self.stack.pop(-1)
                self.stack.append("a")
                print(self.stack)
                self.stack.pop(-1)
                print(self.stack)
                #self.term = yield
                #self.current_state = self.dict_state[self.stack[-1]]()
            #self.term = yield
            else:break


class Validate:
    """Класс валидации выражения"""
    def grep_regex(self, text):
        """Функция проверяет полученный текст на соответствие корректным переходам"""
        # Создаём объект конечного автоматка
        evaluator = LL()
        text = text.lower()
        # перебираем каждый символ полученного выражения
        for term in text:
            # передаем в конечный автомат
            print(term)
            evaluator.send(term)
        # возвращаем соответствие выражения
        return evaluator.does_match()


if name == '__main__':
    Validate().grep_regex("a+a*(a-a)#")
