def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento y el monto final a pagar.

    :param monto_total: float, el monto total de la compra.
    :param porcentaje_descuento: float, porcentaje de descuento (por defecto 10%).
    :return: tuple, (monto_descuento, monto_final)
    """
    monto_descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - monto_descuento
    return monto_descuento, monto_final

if __name__ == "__main__":
    # Primera llamada: solo monto total, usa descuento por defecto
    monto1 = 1000.0
    descuento1, final1 = calcular_descuento(monto1)
    print(f"Compra 1:")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${final1:.2f}\n")

    # Segunda llamada: monto total y porcentaje de descuento especificado
    monto2 = 500.0
    porcentaje2 = 15  # 15% de descuento
    descuento2, final2 = calcular_descuento(monto2, porcentaje2)
    print(f"Compra 2:")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${final2:.2f}")
