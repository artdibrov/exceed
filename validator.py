class Validator:

    def validate(

        self,

        grid

    ):

        floors = sum(

            row.count(".")

            for row in grid

        )

        return floors > 30
