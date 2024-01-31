import translation_handlers.operations as op_handler
import translation_handlers.stack_arithmetic as stack_handler
import translation_handlers.flow as flow_handler
import translation_handlers.function as function_handler

def is_single_operand_op(operand):
    return operand in ['not', 'neg']

def is_double_operation_op(operand):
    return operand in ['add', 'sub', 'and', 'or']

def is_comparision_op(operand):
    return operand in ['eq', 'gt', 'lt']

def is_push(operand):
    return operand == 'push'

def is_pop(operand):
    return operand in 'pop'

def is_flow(operand):
    return 'goto' in operand or operand == 'label'

def is_call(operand):
    return operand == 'call'

def is_function(operand):
    return operand in 'function'

def is_return(operand):
    return operand == 'return'

def translate(vm_code):
    asm_result = []
    for line in vm_code['lines']:
        operand = line['code'][0]
        if is_single_operand_op(operand):
            asm_result += op_handler.handle_single_operand_ops(operand)
        elif is_double_operation_op(operand):
            asm_result += op_handler.handle_double_op(operand)
        elif is_comparision_op(operand):
            asm_result += op_handler.handle_comparison_op(line)
        elif is_push(operand):
            asm_result += stack_handler.handle_push(line)
        elif is_pop(operand):
            asm_result += stack_handler.handle_pop(line)
        elif is_flow(operand):
            asm_result += flow_handler.handle_flow(line)
        elif is_call(operand):
            asm_result += function_handler.handle_call(line)
        elif is_function(operand):
            asm_result += function_handler.handle_function(line)
        elif is_return(operand):
            asm_result += function_handler.handle_return(line)
        else:
            raise Exception(f'Unhandled instruction in line: {line}')
    asm_code = dict(vm_code)
    asm_code['lines'] = asm_result
    return asm_code