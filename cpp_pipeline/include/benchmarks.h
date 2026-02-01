#pragma once
#include <string>
#include <ostream>
#include <filesystem>

class Benchmarks {
public:
    // Ensure the ./cpp_pipeline/benchmarks folder exists
    static void ensureFolder();

    // Generate a unique timestamped filename
    static std::string makeTimestampedFilename();

    // Write metrics from a stream into the CSV file
    static void writeMetrics(const std::string& filename, std::ostream& metrics);

    // Optional helper to write metrics and also echo to console
    static void writeMetricsWithConsole(const std::string& filename, std::ostringstream& metrics);
};
