eggs = int(input("Enter number of eggs"))
eggs_per_box = 6
boxes_filled_with_eggs = eggs // eggs_per_box
eggs_to_fill_uncompleted_box = eggs_per_box - eggs % eggs_per_box
print(f"You have {boxes_filled_with_eggs} boxes of eggs and need {eggs_to_fill_uncompleted_box} "
      f"eggs to fill the last box")
