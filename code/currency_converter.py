def usd_to_gbp(usd):
  Bp=float(usd*.77)
  Bp=round(Bp,2)
  return (Bp)

def usd_to_eur(usd):
  Eu=float(usd*.92)
  Eu=round(Eu,2)
  return (Eu)

def usd_to_cny(usd):
  Yuan=float(usd*6.98)
  Yuan=round(Yuan,2)
  return (Yuan)

def main():
  usd=float(input("Please enter an amount: "))
  call_type=input("Please enter the conversion b for british pounds e for Euros or Y for Yuans.")
  if call_type == "b":
    print(usd_to_gbp(usd))
  elif call_type == "e":
    print(usd_to_eur(usd))
  elif call_type == "y":
    print(usd_to_cny(usd))
  else:
    print("Please input correct conversions.")

  
  
  
  
if __name__== "__main__":
  main()