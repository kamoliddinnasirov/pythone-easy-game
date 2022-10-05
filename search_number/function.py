import random


def sontop(x=100):
    tasodifiy_son = random.randint(1, x)
    print(f"\nMen 1 dan {x} gacha son o'yladim. Topa olasizmi? \n>>>", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting:", end="")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting:", end="")
        else:
            print("Yutdingiz!")
            break

    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar


def sontop_pc(x=100):
    input(f"1 dan {x} gacha son o'ylang va istalgan son kiriting. Men topaman.\n>>>")
    kami = 1
    kopi = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if kami != kopi:
            taxmin = random.randint(kami, kopi)
        else:
            taxmin = kami
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)\n>>>".lower()
        )
        if javob == "-":
            kopi = taxmin - 1
        elif javob == "+":
            kami = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=100):
    yana = True
    while yana:
        taxminlar_pc = sontop_pc(x)
        taxminlar_user = sontop(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):\n>>>"))
        if yana != "yo'q" or yana != 1 or yana !="yoq":
            break



