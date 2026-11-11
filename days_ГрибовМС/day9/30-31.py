import pandas as pd

p = pd.read_csv("products.csv")
p["Стоимость"] = p["Цена"] * p["Количество"]
p = p.sort_values("Стоимость", ascending=False)
p_filtr = p[p["Цена"] > 80]
print(p_filtr)
p_filtr.to_csv("products_result.csv", index=False, encoding="utf-8")
r = pd.read_csv("students.csv")
print(r.info())
r["Percent"] = (r["Посещено"] / 20 * 100).round(1)
r_filtr = r[r["Баллы"] >= 70].sort_values("Баллы", ascending=False)
r_filtr.to_csv("results_output.csv", index=False, encoding="utf-8")