from family import Family
from family import GrandParents
from family import Parents
from family import Children

print("\n== Family Tree ==")
print("1. Input name of a family ")
print("2. Name of the family")
print("3. Input name of grandparents")
print("4. Name of the grandparents")
print("5. Input name of parents")
print("6. Name of the parents")
print("7 Input name of children")
print("8. Name of the children")
print("O. The whole family")
print("E. Exit")
choice = input("choice: ")

# ---------------------------------
the_family_name = Family("No Name")  # default value
there_is_f_name = 1                  # condition to check if name has been updated/inputted
# ---------------------------------
grand_parents = GrandParents("No Name", "No Name")
there_are_grand_parents_name = 1
# ---------------------------------
the_parents = Parents("No Name", "No Name")
there_are_parents_name = 1
# ---------------------------------
the_children = Children("No Name", "No Name")
there_are_children = 1
# ---------------------------------
complete_family_data = 0                   # condition to indicate if there is complete data
# ---------------------------------
family_name = ""
# ---------------------------------


while choice != 'e' and choice != 'E':
    if choice == '1':
        fam_name = input("\nName of a family: ")
        if fam_name.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            fam_name = fam_name.capitalize()
            the_family_name = Family(fam_name)
            there_is_f_name -= 1
            complete_family_data += 1
            family_name = fam_name
            print("\n[ Data updated ]")
    elif choice == '2':
        if there_is_f_name == 0:
            print("\n==============================")
            the_family_name.display_f_name()
            print("==============================")
        else:
            print("\n[ No Name Data ]")

    elif choice == '3':
        gr_pa = input("\nName of grand father: ")
        if gr_pa.isdigit():
            print("\n[ Invalid input - string only ]")
        else:                                            # only if name of grandfather valid then program continue
            gr_ma = input("Name of grand mother: ")
            if gr_ma.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                there_are_grand_parents_name -= 1
                gr_pa = gr_pa.capitalize()
                gr_ma = gr_ma.capitalize()
                grand_parents = GrandParents(gr_pa, gr_ma)
                complete_family_data += 1
                print("\n[ Data updated ]")

    elif choice == '4':
        if there_are_grand_parents_name == 0:
            print("\n==============================")
            grand_parents.the_grand_parents()
            print("==============================")
        else:
            print("\n[ No GrandParents Data ]")

    elif choice == '5':
        papa = input("\nName of father: ")
        if papa.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            mama = input("Name of mother: ")
            if mama.isdigit():
                print("\n[ Invalid input = string only ]")
            else:
                there_are_parents_name -=1
                papa = papa.capitalize()
                mama = mama.capitalize()
                the_parents = Parents(papa,mama)
                complete_family_data += 1
                print("\n[ Data updated ]")

    elif choice == '6':
        if there_are_parents_name == 0:
            print("\n===================")
            the_parents.the_parents()
            print("===================")
        else:
            print("\n[ No Parents Data ]")

    elif choice == '7':
        one_kid = input("\nThe first child's name: ")
        if one_kid.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            two_kid = input("The second child's name: ")
            if two_kid.isdigit():
                print("\n[ Invalid input - string only")
            else:
                there_are_children -= 1
                one_kid = one_kid.capitalize()
                two_kid = two_kid.capitalize()
                the_children = Children(one_kid, two_kid)
                complete_family_data += 1
                print("\n[ Data updated ]")

    elif choice == '8':
        if there_are_children == 0:
            print("\n=========================")
            the_children.the_children()
            print("=========================")
        else:
            print("\n[ No Children Data ]")

    elif choice == 'o':
        if complete_family_data == 4:
            print("\n[ The " + family_name + " Family ]")
            print("==========================")
            the_family_name.display_f_name()
            grand_parents.the_grand_parents()
            the_parents.the_parents()
            the_children.the_children()
            print("==========================")
        else:
            print("\n[ Incomplete data - Input Full Data ]")


    else:
        print("\n[ Invalid choice ]")


    print("\n== Family Tree ==")
    print("1. Input name of a family ")
    print("2. Name of the family")
    print("3. Input name of grandparents")
    print("4. Name of the grandparents")
    print("5. Input name of parents")
    print("6. Name of the parents")
    print("7 Input name of children")
    print("8. Name of the children")
    print("O. The whole family")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")