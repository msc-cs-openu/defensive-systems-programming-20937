#ifndef PROTO_H
#define PROTO_H

#include <cstdint>
#include <string>
#include <vector>

enum class Op : uint8_t
{
    Save = 100,     // Save a file for backup
    Retrieve = 200, // Request to retrieve a file
    Delete = 201,   // Request to delete a file
    List = 202      // Request to list all client files
};

enum class Status : uint16_t
{
    SuccessRetrieved = 210, // Success: File found and retrieved
    SuccessListed = 211,    // Success: List of all files returned to client
    SuccessBackup = 212,    // Success: Backup or file deletion succeeded
    ErrorNotFound = 1001,   // Error: File not found
    ErrorNoFiles = 1002,    // Error: No files exist on the server for this client
    ErrorGeneral = 1003     // Error: General server issue
};

struct Request
{
    uint32_t user_id;             // 4 bytes representing the user
    uint8_t version;              // 1 byte for client version number
    Op op;                        // 1 byte for request code
    uint16_t name_len;            // 2 bytes for file name length
    std::string filename;         // Variable-length file name (ASCII, not null-terminated)
    uint32_t size;                // 4 bytes for the size of the file being sent
    std::vector<uint8_t> payload; // Variable-length file content (binary)
};

struct Response
{
    uint8_t version;              // 1 byte for server version number
    Status status;                // 2 bytes for request status
    uint16_t name_len;            // 2 bytes for file name length
    std::string filename;         // Variable-length file name (ASCII, not null-terminated)
    uint32_t size;                // 4 bytes for the size of the file being sent
    std::vector<uint8_t> payload; // Variable-length file content (binary)
};

#endif // PROTO_H
