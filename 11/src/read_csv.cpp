#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <input.csv>" << std::endl;
        return 1;
    }

    std::ifstream file(argv[1]);
    std::ofstream output("output.txt");

    if (!file)
    {
        std::cerr << "Failed to open input file: " << argv[1] << std::endl;
        return 1;
    }
    if (!output)
    {
        std::cerr << "Failed to open output file: output.txt" << std::endl;
        return 1;
    }

    std::string line;
    std::vector<double> columnSums;

    while (std::getline(file, line))
    {
        std::stringstream ss(line);
        std::string field;
        double rowSum = 0;
        int columnIndex = 0;

        while (std::getline(ss, field, ','))
        {
            field.erase(0, field.find_first_not_of(" \t"));
            field.erase(field.find_last_not_of(" \t") + 1);

            double num;
            std::istringstream iss(field);
            if (iss >> num && iss.eof())
            {
                rowSum += num;
                if (columnIndex >= static_cast<int>(columnSums.size()))
                {
                    columnSums.resize(columnIndex + 1, 0.0);
                }
                columnSums[columnIndex] += num;
            }

            columnIndex++;
        }

        output << "Total of line: " << rowSum << std::endl;
    }

    output << "Sums of columns:\n";
    for (double sum : columnSums)
    {
        output << sum << " ";
    }
    output << std::endl;

    return 0;
}
