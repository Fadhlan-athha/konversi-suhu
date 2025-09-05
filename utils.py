def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan suhu harus 'c', 'f', atau 'k'."

    if dari == "k" and nilai < 0:
        return "Error: Nilai Kelvin tidak boleh negatif."

    # Konversi ke Celsius
    if dari == "c":
        celsius = nilai
    elif dari == "f":
        celsius = (nilai - 32) * 5/9
    elif dari == "k":
        celsius = nilai - 273.15

    # Konversi ke target
    if ke == "c":
        return celsius
    elif ke == "f":
        return (celsius * 9/5) + 32
    elif ke == "k":
        return celsius + 273.15
