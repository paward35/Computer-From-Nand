lines = [
    {'code': 'call sys.init', 'file': 'Sys', 'num': '0'},
    {'code': 'function Main.fibonacci 0', 'file': 'Main', 'num': '11'},
    {'code': 'push argument 0', 'file': 'Main', 'num': '12'},
    {'code': 'push constant 2', 'file': 'Main', 'num': '13'},
    {'code': 'lt', 'file': 'Main', 'num': '14'},
    {'code': 'if-goto N_LT_2', 'file': 'Main', 'num': '15'},
    {'code': 'goto N_GE_2', 'file': 'Main', 'num': '16'},
    {'code': 'label N_LT_2', 'file': 'Main', 'num': '17'},
    {'code': 'push argument 0', 'file': 'Main', 'num': '18'},
    {'code': 'return', 'file': 'Main', 'num': '19'},
    {'code': 'label N_GE_2', 'file': 'Main', 'num': '20'},
    {'code': 'push argument 0', 'file': 'Main', 'num': '21'},
    {'code': 'push constant 2', 'file': 'Main', 'num': '22'},
    {'code': 'sub', 'file': 'Main', 'num': '23'},
    {'code': 'call Main.fibonacci 1', 'file': 'Main', 'num': '24'},
    {'code': 'push argument 0', 'file': 'Main', 'num': '25'},
    {'code': 'push constant 1', 'file': 'Main', 'num': '26'},
    {'code': 'sub', 'file': 'Main', 'num': '27'},
    {'code': 'call Main.fibonacci 1', 'file': 'Main', 'num': '28'},
    {'code': 'add', 'file': 'Main', 'num': '29'},
    {'code': 'return', 'file': 'Main', 'num': '30'},
    {'code': 'function Sys.init 0', 'file': 'Sys', 'num': '42'},
    {'code': 'push constant 4', 'file': 'Sys', 'num': '43'},
    {'code': 'call Main.fibonacci 1', 'file': 'Sys', 'num': '44'},
    {'code': 'label END', 'file': 'Sys', 'num': '45'},
    {'code': 'goto END', 'file': 'Sys', 'num': '46'},
]