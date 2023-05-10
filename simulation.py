import random

class Simulation:
    """
    Contains simulation of Draw Show for MSI 2023.
    Link: https://www.youtube.com/watch?v=v1X9AYoRmpU
    """

    def __init__(self, count_simulation):
        """
        Set up simulation

        Parameters
        ----------
        count_simulation : int
            Number of times to run simulation

        Outputs
        -------
        None.
        """
        self.count_simulation = count_simulation


    def draw_bracket(self):
        """
        Run simulation of Draw Show MSI 2023

        Parameters
        ----------
        None.

        Outputs
        -------
        None.
        """
        count_team_not_placed = 0
        count_two_region_same = 0
        count_exact_scene = 0
        
        for _ in range(self.count_simulation):
            pool_1 = ["KR", "CN"]
            pool_2 = ["NA", "EU"]
            pool_3 = ["KR", "NA", "EU", "CN"]

            bracket = [
                [],
                [],
                [],
                []
            ]

            team = pool_1.pop(random.randrange(len(pool_1)))
            bracket[0].append(team)
            team = pool_1.pop(random.randrange(len(pool_1)))
            bracket[3].append(team)

            team = pool_2.pop(random.randrange(len(pool_2)))
            bracket[1].append(team)
            team = pool_2.pop(random.randrange(len(pool_2)))
            bracket[2].append(team)

            for _ in range(4):
                team = pool_3.pop(random.randrange(len(pool_3)))
                sw_placed = 0
                index_placed = 0
                while sw_placed == 0:
                    if team not in bracket[index_placed] and len(bracket[index_placed]) < 2:
                        bracket[index_placed].append(team)
                        sw_placed = 1
                    elif index_placed < 3:
                        index_placed += 1
                    else:
                        count_team_not_placed += 1
                        break
            
            try:
                bracket_side_1 = [bracket[0][0], bracket[0][1], bracket[1][0], bracket[1][1]]
                bracket_side_2 = [bracket[2][0], bracket[2][1], bracket[3][0], bracket[3][1]]
                set_side_1 = set(bracket_side_1)
                set_side_2 = set(bracket_side_2)

                if len(set_side_1) == 2 and len(set_side_2) == 2:
                    count_two_region_same += 1
                    if {"NA", "CN"} == set_side_1 or {"NA", "CN"} == set_side_2:
                        count_exact_scene += 1
            except:
                pass

        return (count_team_not_placed, count_two_region_same, count_exact_scene)



if __name__ == "__main__":
    count_simulation = 1000000
    sim = Simulation(count_simulation)
    count_team_not_placed, count_two_region_same, count_exact_scene = sim.draw_bracket()
    print(
        f"\nSimulated Draw Show {count_simulation} Times:\n", 
        " Unresolved draws:", count_team_not_placed, 
        f"({int((count_team_not_placed / count_simulation) * 100)}%)",
        f"\n  Resolved draws: {int(count_simulation - count_team_not_placed)}", 
        f"({int((int(count_simulation - count_team_not_placed) / count_simulation) * 100)}%)",
        "\n    Draws where only two regions occupy each side of bracket:", count_two_region_same, 
        f"({int((count_two_region_same / int(count_simulation - count_team_not_placed)) * 100)}%)",
        "\n    Draws exactly like MSI 2023:", count_exact_scene, 
        f"({int((count_exact_scene / int(count_simulation - count_team_not_placed)) * 100)}%)", "\n"
    )