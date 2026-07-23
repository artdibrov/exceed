class Statistics:

    def collect(

        self,

        grid

    ):

        stats = {}

        for symbol in [

            "#",

            ".",

            "+",

            "~",

            "^",

            "@"

        ]:

            stats[symbol] = sum(

                row.count(symbol)

                for row in grid

            )

        return stats

    def print(

        self,

        stats

    ):

        print("Map Statistics\n")

        for k, v in stats.items():

            print(

                f"{k}: {v}"

            )
