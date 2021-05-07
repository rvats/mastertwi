using Microsoft.Azure.Management.Compute.Fluent.Models;
using Microsoft.Azure.Management.Fluent;
using Microsoft.Azure.Management.ResourceManager.Fluent;
using Microsoft.Azure.Management.ResourceManager.Fluent.Core;
using System;

namespace AzureWalkThrough
{
    class Program
    {
        static void Main(string[] args)
        {
            var subscriptionId = "0009fc4d-e310-4e40-8e63-c48a23e9cdc1";
            var subscriptionName = "SQL IaaS R&D 1";
            var clientId = "ba82b2ae-8e84-48ad-90fb-60f0ec111c44";
            var clientSecret = "clientSecret";
            var tenantId = "72f988bf-86f1-41af-91ab-2d7cd011db47";
            var groupName = "sampleResourceGroup";
            var vmName = "TestRAV"+DateTime.Now.Ticks.ToString();
            var location = Region.USSouthCentral;

            var credentials = SdkContext.AzureCredentialsFactory
                .FromServicePrincipal(clientId, clientSecret, tenantId, AzureEnvironment.AzureGlobalCloud);


            var azure = Azure
                .Configure()
                .WithLogLevel(HttpLoggingDelegatingHandler.Level.Basic)
                .Authenticate(credentials)
                .WithDefaultSubscription();

            var resourceGroup = azure.ResourceGroups.Define(groupName)
                .WithRegion(location)
                .Create();

            var network = azure.Networks.Define("sampleVirtualNetwork")
              .WithRegion(location)
              .WithExistingResourceGroup(groupName)
              .WithAddressSpace("10.0.0.0/16")
              .WithSubnet("sampleSubNet", "10.0.0.0/24")
              .Create();

            var publicIPAddress = azure.PublicIPAddresses.Define("samplePublicIP")
                .WithRegion(location)
                .WithExistingResourceGroup(groupName)
                .WithDynamicIP()
                .Create();

            var networkInterface = azure.NetworkInterfaces.Define("sampleNetWorkInterface")
                .WithRegion(location)
                .WithExistingResourceGroup(groupName)
                .WithExistingPrimaryNetwork(network)
                .WithSubnet("sampleSubNet")
                .WithPrimaryPrivateIPAddressDynamic()
                .WithExistingPrimaryPublicIPAddress(publicIPAddress)
                .Create();

            var availabilitySet = azure.AvailabilitySets.Define("sampleAvailabilitySet")
                .WithRegion(location)
                .WithExistingResourceGroup(groupName)
                .WithSku(AvailabilitySetSkuTypes.Aligned)
                .Create();

            azure.VirtualMachines.Define(vmName)
                .WithRegion(location)
                .WithExistingResourceGroup(groupName)
                .WithExistingPrimaryNetworkInterface(networkInterface)
                .WithLatestWindowsImage("MicrosoftWindowsServer", "WindowsServer", "2012-R2-Datacenter")
                .WithAdminUsername("sampleUser")
                .WithAdminPassword("Sample123467")
                .WithComputerName(vmName)
                .WithExistingAvailabilitySet(availabilitySet)
                .WithSize(VirtualMachineSizeTypes.StandardB1s)
                .Create();
        }
    }
}