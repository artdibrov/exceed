class Exporter:

    def save(

        self,

        grid,

        filename="map.txt"

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            for row in grid:

                file.write(

                    "".join(row)

                )

                file.write("\n")
