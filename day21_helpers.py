def parse_shop_menu(categories):
    items_dict = {}
    for category in categories:
        parsed_category = parse_table(category)
        category_name = parsed_category[0]
        category_items = parsed_category[1]
        items_dict[category_name] = category_items
    return items_dict


def parse_table(str_table):
    """Return tuple (table_title, table_items_dict) from a string

       The table should be of the following format

       {table_title}: col_header0 col_header1 col_header2 ...
       row_key0       int         int         int  
       row_key1       int         int         int  
       row_key2       int         int         int  
       ...

       table_items_dictionary = {
                            row_key0: {
                                col_header0: int,
                                col_header1: int,
                                col_header2: int,
                                },

                            row_key1: { 
                                ... 
                                },

                            ...
                            }
    """
    str_table_lst = str_table.splitlines()
    header_row = str_table_lst[0]

    # title is everything on first row until colon
    colon_i = header_row.index(":")
    table_title = header_row[:colon_i].strip()
    col_label_lst = header_row[colon_i + 2:].split()
    n_cols = len(col_label_lst)
    
    table_items_dict = {}
    for row in str_table_lst[1:]:
        row = row.split()

        # Dealing with spaces in row label
        row_label = ' '.join(row[:-n_cols])
        values = map(int, row[-n_cols:])
        table_items_dict[row_label] = dict(zip(col_label_lst, values))

    return (table_title, table_items_dict)


def parse_boss(filename):
    with open(filename, "r") as f:
        boss_stats = {}
        for line in f.readlines():
            k, v = line.split(": ")
            boss_stats[k] = int(v)
    boss_stats["Name"] = "Boss"
    return boss_stats


def parse_shop(filename):
    with open(filename, "r") as f:
        categories = f.read().split("\n\n")
        shop_items_dict = parse_shop_menu(categories)
    return shop_items_dict

if __name__ == "__main__":
    shop = parse_shop("shop.txt")
    boss = parse_boss("boss.txt")
    print(shop)
    print(boss)
