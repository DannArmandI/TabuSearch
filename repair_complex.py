def repair_solution_complex(instance, neighbour, missing_rows):
    "asdasd"
    while missing_rows:
        best_trade_off=10000
        best_column_index=0
        best_finded_rows=[]
        for (i, column) in enumerate(neighbour.columns):
            if not missing_rows:
                break
            if column:
                continue
            else:
                finded_rows = [
                    x for x in instance.columns[i].active_rows if x in missing_rows]
                if finded_rows:
                    trade_off=instance.columns[i].cost/len(finded_rows)
                    if best_trade_off >= trade_off:
                        best_trade_off=trade_off
                        best_column_index = i
                        best_finded_rows=finded_rows
        neighbour.columns[best_column_index] = 1
        neighbour.fitness += instance.columns[best_column_index].cost
        for finded_row in best_finded_rows:
            missing_rows.remove(finded_row)
            neighbour.rows[finded_row]+=1