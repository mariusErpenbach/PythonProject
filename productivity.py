def calc_productivity(work_output, work_input):
    """Calculates productivity as output/input"""
    return work_output / work_input


def work_input_saving(work_output, work_input, best_productivity):
    """Calculates the potential work input savings"""
    optimal_input = work_output / best_productivity  # Required input at best productivity
    return work_input - optimal_input  # Saved work hours


def best_productivity(statistic):
    """Finds the facility with the highest productivity"""
    best = ["", 0]
    for item in statistic:
        productivity = calc_productivity(item["Produktionsmenge"], item["Arbeitsstunden"])
        if productivity > best[1]:
            best[0] = item["Fertigungsstätte"]
            best[1] = productivity
    return best


def analyze_productivity(statistic):
    """Compares all facilities to the best productivity"""
    best_location, best_prod = best_productivity(statistic)

    print(f"Best productivity: {best_prod:.3f} from {best_location}\n")  # More decimal places

    for item in statistic:
        name = item["Fertigungsstätte"]
        hours = item["Arbeitsstunden"]
        output = item["Produktionsmenge"]
        prod = calc_productivity(output, hours)
        saving = work_input_saving(output, hours, best_prod)

        print(f"{name}:")
        print(f"  Productivity: {prod:.3f}")  # More decimal places
        print(f"  Potential savings: {saving:.3f} hours" if saving > 0 else "  No savings possible")
        print("-" * 40)


# Example data
statistik_example = [
    {"Fertigungsstätte": "Hamburg", "Arbeitsstunden": 5200, "Produktionsmenge": 1200},
    {"Fertigungsstätte": "Hannover", "Arbeitsstunden": 3200, "Produktionsmenge": 700},
    {"Fertigungsstätte": "Düsseldorf", "Arbeitsstunden": 12300, "Produktionsmenge": 3400},
    {"Fertigungsstätte": "Frankfurt a. M.", "Arbeitsstunden": 23200, "Produktionsmenge": 5600},
    {"Fertigungsstätte": "Regensburg", "Arbeitsstunden": 16900, "Produktionsmenge": 4200},
    {"Fertigungsstätte": "Dresden", "Arbeitsstunden": 10400, "Produktionsmenge": 2900},
]

# Run analysis
analyze_productivity(statistik_example)
