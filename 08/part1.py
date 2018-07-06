
from collections import defaultdict

def read_input(input_filename):
    program = []
    with open(input_filename, "r") as input_file:
        input_rows = input_file.read().strip().split("\n")
        rows = [row.split(" if ") for row in input_rows]
        for row in rows:
            output_register, operator, change_value = row[0].split(" ")
            input_register, comp_operator, comp_value = row[1].split(" ")
            change_value = int(change_value)
            comp_value = int(comp_value)
            program.append({"output_register": output_register,
                            "operator": operator,
                            "change_value": change_value,
                            "input_register": input_register,
                            "comp_operator": comp_operator,
                            "comp_value": comp_value})
    return program


def execute_operation(line, registers):
    if line["operator"] == "inc":
        registers[line["output_register"]] += line["change_value"]
    elif line["operator"] == "dec":
        registers[line["output_register"]] -= line["change_value"]
    else:
        raise Exception("I only know how to inc or dec!")


def run_program(program):
    registers = defaultdict(int)

    for line in program:
        if line["comp_operator"] == "<":
            if registers[line["input_register"]] < line["comp_value"]:
                execute_operation(line, registers)
        elif line["comp_operator"] == "<=":
            if registers[line["input_register"]] <= line["comp_value"]:
                execute_operation(line, registers)
        elif line["comp_operator"] == ">":
            if registers[line["input_register"]] > line["comp_value"]:
                execute_operation(line, registers)
        elif line["comp_operator"] == ">=":
            if registers[line["input_register"]] >= line["comp_value"]:
                execute_operation(line, registers)
        elif line["comp_operator"] == "==":
            if registers[line["input_register"]] == line["comp_value"]:
                execute_operation(line, registers)
        elif line["comp_operator"] == "!=":
            if registers[line["input_register"]] != line["comp_value"]:
                execute_operation(line, registers)
        else:
            raise Exception("I don't know that operator.")

    return max(registers.values())


if __name__ == "__main__":
    INPUT = read_input("08/input.txt")
    print(run_program(INPUT))
