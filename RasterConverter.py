import os
import re


class RasterLayer:
	def __init__(self, xcorner: str, ycorner: str, cell_size: str, none_value: str, data: list[str]):
		self.xcorner: float = float(xcorner)
		self.ycorner:float = float(ycorner)
		self.cell_size: float = float(cell_size)
		self.none_value: int = int(none_value)

		self.data: list[str] = data
		self.output: list[list[str]] = []

		self.calculate()
		
	def calculate(self):
		self.output.clear()

		xcorner: float = self.xcorner
		ycorner: float = self.ycorner

		i = 0
		for row in self.data:
			

			data = row.split(" ")
			xcorner = self.xcorner

			for x in data:
				csv_row: list[str] = []
				csv_row.append(str(xcorner))
				csv_row.append(str(ycorner))				

				value: str = ""
				if int(float(x)) == none_value:
					value = "NA"
				else:
					value = x
				
				
				csv_row.append(str(value))
				xcorner += cell_size
				self.output.append(csv_row)
			ycorner += cell_size
			i += 1

	def to_csv_string(self) -> str:
		csv_string: str = "\"\",\"X\",\"Y\",\"Value\"\n"
		for i, row in enumerate(self.output):
			csv_string += "\"" + str(i) + "\"," + ",".join(row) + "\n"

		return csv_string



if __name__ == "__main__":
	for file_name in os.listdir("asc files"):
		with open("asc files/" + file_name, "r") as file:
			file.readline()
			file.readline()

			xcorner: float = float(file.readline().split(" ")[1])
			ycorner: float = float(file.readline().split(" ")[1])
			cell_size: float = float(file.readline().split(" ")[1])
			none_value: int = int(file.readline().split(" ")[1])

			raster_layer: RasterLayer = RasterLayer(xcorner, ycorner, cell_size, none_value, file.readlines())

		
		file_name = re.sub(".asc", ".csv", file_name)
		with open("csv files/" + file_name, "w") as file:
			file.write(raster_layer.to_csv_string())


