def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows <= 2 or num_columns <= 2:
        return 'ОШИБКА! Размерности таблицы должны быть больше 2!'
    else:
        list_1 = []
        for k in range(num_columns):
            list_1.append(k + 1)
        print(*list_1)
        #print(*range(1, num_columns + 1))
        
        for row in range(1, num_rows + 1):
            res=[]
            for col in range(1, num_columns):
                if col == 1:
                    print(row, end='\t')
                elif row == 1:
                    print(col, end='\t')
                else:
                    if col == num_columns:
                        print(operation(row, col), end='')
                    else:
                        print(operation(row, col), end="\t")
        print()
    
print_operation_table(lambda x, y: x * y, 3, 3)