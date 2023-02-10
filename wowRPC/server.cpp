#include <iostream>
#include "WowRPCServer.H"

int main()
{
  std::string server_addr("0.0.0.0:50051");
  WowFSServiceImpl service;

  grpc::EnableDefaultHealthCheckService( true );
  grpc::reflection::InitProtoReflectionServerBuilderPlugin();
  grpc::ServerBuilder builder;

  builder.AddListeningPort( server_addr, grpc::InsecureServerCredentials() );
  builder.RegisterService( &service );

  std::unique_ptr<grpc::Server> server( builder.BuildAndStart() );
  std::cout << "Server listening on " << server_addr << std::endl;

  server->Wait();

  return 0;
}
