dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']
item_to_find=['TAA']
item_found=False
for i in range(len(dna_sequence)):
  if dna_sequence[i]==item_to_find:
    item_found=True
    break
if item_found==True:
  print("Item Found")
else:
  print("Item not found")