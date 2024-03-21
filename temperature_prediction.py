import math

class HeatSource:
    def __init__(self, surface_area, initial_temperature):
        self.surface_area = surface_area
        self.initial_temperature = initial_temperature

class HeatTransferCoefficient:
    def __init__(self, coefficient_value):
        self.coefficient_value = coefficient_value

class FluidProperties:
    def __init__(self, temperature):
        self.temperature = temperature

class TemperaturePredictionResult:
    def __init__(self, predicted_temperature):
        self.predicted_temperature = predicted_temperature

def predict_temperature(heat_source, heat_transfer_coefficient, fluid_properties):
    predicted_temperature = fluid_properties.temperature + (heat_source.initial_temperature - fluid_properties.temperature) * math.exp(-heat_transfer_coefficient.coefficient_value * heat_source.surface_area)
    return TemperaturePredictionResult(predicted_temperature)

def main():
    print("Welcome to the Heat Source Temperature Prediction Calculator")
    surface_area = float(input("Enter the surface area of the heat source (in m^2): "))
    initial_temperature = float(input("Enter the initial temperature of the heat source (in °C): "))
    coefficient_value = float(input("Enter the convective heat transfer coefficient (in W/m^2K): "))
    fluid_temperature = float(input("Enter the temperature of the surrounding fluid (in °C): "))

    heat_source = HeatSource(surface_area, initial_temperature)
    heat_transfer_coefficient = HeatTransferCoefficient(coefficient_value)
    fluid_properties = FluidProperties(fluid_temperature)

    result = predict_temperature(heat_source, heat_transfer_coefficient, fluid_properties)
    print(f"The predicted temperature of the heat source is: {result.predicted_temperature:.2f} °C")

if __name__ == "__main__":
    main()
