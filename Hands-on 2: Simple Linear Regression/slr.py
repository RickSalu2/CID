# -*- coding: utf-8 -*-
"""SLR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NTsF080BoLL74pD61vdXojuvTjif-brT
"""

class SimpleLinearRegression:
    def __init__(self):

        self.b0 = 0.0  # Intercepto de la línea de regresión
        self.b1 = 0.0  # Pendiente de la línea de regresión

    def fit(self, X, Y):

        n = len(X)

        if n == 0 or len(Y) != n:
            raise ValueError("Las listas de datos deben tener la misma longitud y no estar vacías.")

        # Cálculo de la media de X y de Y.
        mean_x = sum(X) / n
        mean_y = sum(Y) / n

        numerator = 0.0   # Acumula el producto de las diferencias de cada valor con la media.
        denominator = 0.0 # Acumula el cuadrado de la diferencia de cada valor respecto a la media.

        # Se recorre cada elemento de los datos para realizar la suma acumulativa.
        for i in range(n):
            numerator += (X[i] - mean_x) * (Y[i] - mean_y)
            denominator += (X[i] - mean_x) ** 2

        # Comprobar que el denominador no sea cero para evitar división por cero.
        if denominator == 0:
            raise ValueError("Error en el cálculo: denominador es cero, no se puede calcular la pendiente.")

        # Calcular la pendiente b1 y el intercepto b0, usando las fórmulas estadísticas.
        self.b1 = numerator / denominator
        self.b0 = mean_y - self.b1 * mean_x

    def predict(self, x):

        # Si la entrada es una lista, se genera una lista de predicciones.
        if isinstance(x, list):
            return [self.b0 + self.b1 * xi for xi in x]
        else:
            return self.b0 + self.b1 * x

    def __str__(self):

        return f"y = {self.b0:.4f} + {self.b1:.4f} x"


if __name__ == '__main__':

    # Dataset del Caso Benetton (valores de ejemplo hardcoded)
    Advertising = [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 120.2, 8.6, 199.8]
    Sales       = [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 12.8, 18.9, 8.1, 12.8]

    # Se crea una instancia del modelo de regresión lineal.
    model = SimpleLinearRegression()

    # Se entrena (ajusta) el modelo con los datos de Advertising y Sales.
    model.fit(Advertising, Sales)

    # Se imprime la ecuación de regresión obtenida tras ajustar el modelo, mostrando los valores de b0 y b1.
    print("Ecuación de Regresión:", model)

    # Se definen cinco nuevos valores de Advertising para los cuales se realizarán las predicciones.
    test_advertising_values = [50, 100, 150, 200, 250]

    predictions = model.predict(test_advertising_values)

    print("\nPredicciones para valores de Advertising:")
    for adv, pred in zip(test_advertising_values, predictions):
        print(f"Advertising: {adv} --> Predicted Sales: {pred:.4f}")