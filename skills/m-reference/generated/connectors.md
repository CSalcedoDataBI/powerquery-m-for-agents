# M connector entry points

273 connector functions from `#shared` (`desktop` 2.157.879.0): functions the engine gives no category, from a prefix no library function uses. Many carry no description. Flags as in `catalog.md`.
Open one card: `library/<file>.md`, where <file> is the name in lower case with every run of non-alphanumerics as one dash (`Table.AddColumn` -> `table-addcolumn`).

| Function | Connector | Returns | Flags | Summary |
|---|---|---|---|---|
| `Acterys.Contents` | Acterys | any |  |  |
| `Actian.Contents` | Actian | any |  |  |
| `ADPAnalytics.Contents` | ADPAnalytics | any |  |  |
| `AmazonAthena.Databases` | AmazonAthena | table |  | This function sends basic authentication info |
| `AmazonOpenSearchService.Contents` | AmazonOpenSearchService | table |  |  |
| `AmazonRedshift.Database` | AmazonRedshift | table |  | Import data from an Amazon Redshift database. |
| `Anaplan.Contents` | Anaplan | table |  |  |
| `ApacheHiveLLAP.Database` | ApacheHiveLLAP | table |  | Import data from a Hive LLAP |
| `ApacheSpark.Tables` | ApacheSpark | table |  | Returns a table listing the tables on the specified Spark cluster. |
| `appFigures.Content` | appFigures | any |  |  |
| `appFigures.Tables` | appFigures | table |  |  |
| `AptixInsights.Feed` | AptixInsights | table |  | Use the Aptix Insights Platform OData API to build powerful reports and dashboards. |
| `Asana.Tables` | Asana | table |  | Returns a table with Asana task data |
| `AssembleViews.Contents` | AssembleViews | table |  | Access views created within Assemble Insight |
| `AssembleViews.Feed` | AssembleViews | table |  | Access views created within Assemble Insight |
| `AtScale.Cubes` | AtScale | table |  | Import/DirectQuery cube data from an AtScale. |
| `AutodeskConstructionCloud.Contents` | AutodeskConstructionCloud | table |  |  |
| `AutodeskConstructionCloud.Feed` | AutodeskConstructionCloud | table |  |  |
| `AutomationAnywhere.Feed` | AutomationAnywhere | table |  | Automation Anywhere - Login |
| `AutomyDataAnalytics.Contents` | AutomyDataAnalytics | table |  |  |
| `AzureCosmosDBForMongoDBvCore.Contents` | AzureCosmosDBForMongoDBvCore | table |  | Azure Cosmos DB for MongoDB vCore |
| `AzureCostManagement.Contents` | AzureCostManagement | table |  |  |
| `AzureCostManagement.Tables` | AzureCostManagement | table |  | Azure Cost Management |
| `AzureDataExplorer.Contents` | AzureDataExplorer | table |  | Imports data from Azure Data Explorer (Kusto) |
| `AzureDataExplorer.Databases` | AzureDataExplorer | list |  |  |
| `AzureDataExplorer.KqlDatabase` | AzureDataExplorer | table |  | Import data from Fabric Kusto cluster in discovery mode. |
| `AzureDeviceRegistry.Query` | AzureDeviceRegistry | table |  | Connector to pull Assets and Devices from Azure Device Registry |
| `AzureDevOpsServer.AccountContents` | AzureDevOpsServer | table |  | Enter Url of your Azure DevOps Analytics Service. |
| `AzureDevOpsServer.AnalyticsViews` | AzureDevOpsServer | table |  | Enter organization and project names. |
| `AzureDevOpsServer.Feed` | AzureDevOpsServer | table |  | Azure DevOps Services Feed |
| `AzureDevOpsServer.Views` | AzureDevOpsServer | table |  | Enter organization and project names. |
| `AzureEnterprise.Contents` | AzureEnterprise | binary |  | Enter the URL of the Azure Enterprise REST API endpoint associated with your enrollment |
| `AzureEnterprise.Tables` | AzureEnterprise | table |  | Enter the URL of the Azure Enterprise REST API endpoint associated with your enrollment |
| `AzureHiveLLAP.Database` | AzureHiveLLAP | table |  | Import data from HDInsight Interactive Query |
| `AzureResourceGraph.Query` | AzureResourceGraph | table |  | See https://learn.microsoft.com/azure/governance/resource-graph/samples/starter?tabs=azure-cli for starter query sample… |
| `AzureSpark.Tables` | AzureSpark | table |  | List the tables in an Azure Spark instance. |
| `AzureTimeSeriesInsights.Contents` | AzureTimeSeriesInsights | table |  |  |
| `BI360.Contents` | BI360 | table |  | Retrieves a Navigation Table populated with the enabled tables for a given token |
| `BIConnector.Contents` | BIConnector | table |  | Enter connection information |
| `BitSightSecurityRatings.Contents` | BitSightSecurityRatings | any |  |  |
| `Bloomberg.Query` | Bloomberg | table |  | Used for retrieving Bloomberg data |
| `BQECore.Contents` | BQECore | any |  |  |
| `BQL.Query` | BQL | table |  | Used for retrieving Bloomberg data |
| `BuildingConnected.Contents` | BuildingConnected | table |  | Returns a table of entities for the given url and entity name. |
| `CCHTagetik.Contents` | CCHTagetik | table |  | Wolters Kluwer CCH Tagetik |
| `CCHTagetik.Contents2` | CCHTagetik | table |  | Wolters Kluwer CCH Tagetik |
| `CCHTagetik.Contents3` | CCHTagetik | table |  | Wolters Kluwer CCH Tagetik |
| `CCHTagetik.Contents4` | CCHTagetik | table |  | Wolters Kluwer CCH Tagetik |
| `CDataConnectCloud.Contents` | CDataConnectCloud | table |  | Returns a table with relevant data from the connected data source in CData Connect Cloud. |
| `CDataConnectCloud.ContentsV2` | CDataConnectCloud | table |  | Returns a table with relevant data from the connected data source in CData Connect Cloud. |
| `Cds.Contents` | Cds | any |  |  |
| `Cds.Entities` | Cds | table |  | Connect to your Common Data Service instance (Dynamics 365 and PowerApps). |
| `Celonis.KnowledgeModels` | Celonis | table |  |  |
| `Celonis.Navigation` | Celonis | table |  |  |
| `Cherwell.SavedSearches` | Cherwell | table |  | Returns the results of a Saved Search from a Cherwell Service Management REST API (requires CSM version 10.2 or later). |
| `ClickHouse.Database` | ClickHouse | table |  | ClickHouse ODBC connector for Power Query |
| `CloudBluePSA.Feed` | CloudBluePSA | table |  | This function will resolve the page limitation issue and will retrieve and combine all pages of data returned by the AP… |
| `Cognite.Contents` | Cognite | table |  | Cognite Data Fusion (CDF) |
| `CogniteDataSource.Contents` | CogniteDataSource | table |  | Cognite Data Fusion (CDF) |
| `CommonDataService.Database` | CommonDataService | table |  | Connect to your Dataverse instance (Dynamics 365 and PowerApps). |
| `CosmosDB.Contents` | CosmosDB | table |  |  |
| `CustomerInsights.Contents` | CustomerInsights | table |  |  |
| `Databricks.Catalogs` | Databricks | table |  |  |
| `Databricks.Contents` | Databricks | table |  |  |
| `Databricks.Query` | Databricks | function |  | Define a Databricks data source for running SQL queries |
| `DatabricksMultiCloud.Catalogs` | DatabricksMultiCloud | table |  |  |
| `DatabricksMultiCloud.Query` | DatabricksMultiCloud | function |  | Define a Databricks data source for running SQL queries |
| `DataLake.Contents` | DataLake | table |  | Enter the URL of your Azure Data Lake Storage Gen1 account. |
| `DataLake.Files` | DataLake | table |  | Enter the URL of your Azure Data Lake Storage account. |
| `DataVirtuality.Database` | DataVirtuality | table |  | Data Virtuality LDW |
| `DataWorld.Contents` | DataWorld | table |  |  |
| `DataWorld.Dataset` | DataWorld | table |  | Retrieves a dataset from Data.World |
| `DCWInsights.Feed` | DCWInsights | table |  | Use the DCW Integrations Platform OData API to build powerful reports and dashboards. |
| `DeltaSharing.Contents` | DeltaSharing | table |  |  |
| `Denodo.Contents` | Denodo | table |  | The Denodo Connector allows you to connect to Denodo's VDP server from PowerBI |
| `DocumentDB.Contents` | DocumentDB | table |  | Enter the URL of an Azure Cosmos DB account. |
| `Dremio.Databases` | Dremio | table |  | Returns a table listing the datasets on Dremio Server. |
| `Dremio.DatabasesV300` | Dremio | table |  | Returns a table listing the datasets on Dremio Server. |
| `Dremio.DatabasesV370` | Dremio | table |  | Returns a table listing the datasets on Dremio Server. |
| `DremioCloud.Databases` | DremioCloud | table |  | Returns a table listing the datasets in the specified project on Dremio Cloud. |
| `DremioCloud.DatabasesByServer` | DremioCloud | table |  | Returns a table listing the datasets on the specified server on Dremio Cloud. |
| `DremioCloud.DatabasesByServerV330` | DremioCloud | table |  | Returns a table listing the datasets on the specified server on Dremio Cloud. |
| `DremioCloud.DatabasesByServerV360` | DremioCloud | table |  | Returns a table listing the datasets on the specified server on Dremio Cloud. |
| `DremioCloud.DatabasesByServerV370` | DremioCloud | table |  | Returns a table listing the datasets on the specified server on Dremio Cloud. |
| `DremioTesting.Contents` | DremioTesting | any |  |  |
| `Dynamics365BusinessCentral.ApiContents` | Dynamics365BusinessCentral | table |  | Enter your Dynamics 365 Business Central environment and company. |
| `Dynamics365BusinessCentral.ApiContentsWithOptions` | Dynamics365BusinessCentral | table |  | Enter your Dynamics 365 Business Central environment and company. |
| `Dynamics365BusinessCentral.Contents` | Dynamics365BusinessCentral | table |  | Enter your Dynamics 365 Business Central environment and company. |
| `Dynamics365BusinessCentral.EnvironmentContents` | Dynamics365BusinessCentral | table |  | Enter your Dynamics 365 Business Central environment and company. |
| `Dynamics365BusinessCentralOnPremises.Contents` | Dynamics365BusinessCentralOnPremises | table |  | Enter the URL of your Dynamics 365 Business Central (on-premises) OData service endpoint. |
| `DynamicsNav.Contents` | DynamicsNav | table |  | Enter the URL of your Dynamics NAV OData service endpoint. |
| `DynatraceGrail.Contents` | DynatraceGrail | table |  | DQL Connector can be used to fetch data from Grail using DQL custom query or by selecting tables. |
| `EduFrame.Contents` | EduFrame | table |  |  |
| `Emigo.Contents` | Emigo | table |  | The purpose of the method is to set parameters for odata feed data source calls, thus the non-function calls may be lim… |
| `Emigo.GetExtractFunction` | Emigo | any |  |  |
| `EmigoDataSourceConnector.GetExtractFunction` | EmigoDataSourceConnector | any |  |  |
| `EntersoftBusinessSuite.Contents` | EntersoftBusinessSuite | any |  |  |
| `EQuIS.Contents` | EQuIS | table |  |  |
| `eWayCRM.Contents` | eWayCRM | table |  |  |
| `eWayCRM.Contents2` | eWayCRM | table |  |  |
| `ExactOnlinePremium.Contents` | ExactOnlinePremium | table |  | Get data directly from Exact Online Premium |
| `Exasol.Database` | Exasol | table |  | Exasol |
| `Fabric.Warehouse` | Fabric | table |  | Imports data from Warehouse |
| `FabricSql.Contents` | FabricSql | table |  | Imports data from SQL database Instance in Fabric |
| `FactSetAnalytics.ConnectionCheck` | FactSetAnalytics | any |  |  |
| `FactSetAnalytics.Contents` | FactSetAnalytics | table |  |  |
| `FactSetAnalytics.Functions` | FactSetAnalytics | table |  |  |
| `FactSetRMS.Functions` | FactSetRMS | table |  |  |
| `Fhir.Contents` | Fhir | table |  |  |
| `Foundry.Contents` | Foundry | table |  | Connect to Palantir Foundry datasets. |
| `Funnel.Contents` | Funnel | table |  | Returns a navigation table to help the user navigate their Workspaces and respective Data Shares. |
| `Github.Contents` | Github | any |  |  |
| `Github.PagedTable` | Github | any |  |  |
| `Github.Tables` | Github | table |  | Enter the GitHub repository owner and the repository name. |
| `GoogleBigQuery.Database` | GoogleBigQuery | table |  | Import data from a Google BigQuery database. |
| `GoogleBigQueryAad.Database` | GoogleBigQueryAad | table |  | Import data from a Google BigQuery database using Microsoft Entra ID |
| `GoogleSheets.Contents` | GoogleSheets | table |  | Imports data from GoogleSheets |
| `HexagonSmartApi.ApplySelectList` | HexagonSmartApi | table |  |  |
| `HexagonSmartApi.ApplyUnitsOfMeasure` | HexagonSmartApi | any |  |  |
| `HexagonSmartApi.ExecuteParametricFilterOnFilterRecord` | HexagonSmartApi | any |  |  |
| `HexagonSmartApi.ExecuteParametricFilterOnFilterUrl` | HexagonSmartApi | any |  |  |
| `HexagonSmartApi.Feed` | HexagonSmartApi | table |  | Returns a table from a Hexagon PPM Smart API OData feed. |
| `HexagonSmartApi.GenerateParametricFilterByFilterSourceType` | HexagonSmartApi | any |  |  |
| `HexagonSmartApi.GetODataMetadata` | HexagonSmartApi | any |  |  |
| `HexagonSmartApi.Typecast` | HexagonSmartApi | function |  | Function to return a table representing an OData entity typecast from the target entity. |
| `Impala.Database` | Impala | table |  | Import data from an Impala cluster |
| `Indexima.Database` | Indexima | table |  | Connection to Indexima Data Hub |
| `IndustrialAppStore.NavigationTable` | IndustrialAppStore | any |  |  |
| `InformationGrid.Contents` | InformationGrid | table |  | Retrieves information from authorised BI services available on the given server |
| `IntersystemsHealthInsight.Database` | IntersystemsHealthInsight | table |  | InterSystems Health Insight |
| `Intune.Contents` | Intune | table |  | Intune Data Warehouse |
| `IntuneV2.Contents` | IntuneV2 | table |  | Intune Data Warehouse V2 |
| `inwink.ScopeContents` | inwink | table |  | inwink data |
| `IRIS.Database` | IRIS | table |  | InterSystems IRIS |
| `JamfPro.Contents` | JamfPro | text |  |  |
| `JethroODBC.Database` | JethroODBC | table |  |  |
| `Kognitwin.Contents` | Kognitwin | table |  |  |
| `Kusto.Contents` | Kusto | table |  | Imports data from Azure Data Explorer (Kusto) |
| `Kusto.Databases` | Kusto | list |  |  |
| `kxkdbinsightsenterprise.Contents` | kxkdbinsightsenterprise | table |  | Imports data from KX kdb Insights Enterprise |
| `Kyligence.Database` | Kyligence | table |  | Connect your Kyligence |
| `KyvosODBC.Databases` | KyvosODBC | table |  | Returns a table listing the datasets on Kyvos Server. |
| `Lakehouse.Contents` | Lakehouse | table |  | Import data from a Lakehouse |
| `LEAP.Contents` | LEAP | table |  | Returns a table with relevant LEAP data. |
| `Linkar.Contents` | Linkar | table |  |  |
| `LinkedIn.SalesContracts` | LinkedIn | table |  |  |
| `LinkedIn.SalesContractsWithReportAccess` | LinkedIn | table |  |  |
| `LinkedIn.SalesNavigator` | LinkedIn | table |  | LinkedIn Sales Navigator |
| `LinkedIn.SalesNavigatorAnalytics` | LinkedIn | table |  |  |
| `LinkedIn.SalesNavigatorAnalyticsImpl` | LinkedIn | any |  |  |
| `LinkedInLearning.Contents` | LinkedInLearning | any |  |  |
| `MailChimp.Collection` | MailChimp | table |  | Returns a table with data from a MailChimp endpoint. |
| `MailChimp.Instance` | MailChimp | table |  | Returns raw response results from a MailChimp API endpoint. |
| `MailChimp.Tables` | MailChimp | table |  |  |
| `MailChimp.TablesV2` | MailChimp | table |  | Returns a table with key MailChimp data. |
| `MariaDB.Contents` | MariaDB | table |  | Returns a navigation table. |
| `Marketo.Activities` | Marketo | table |  | Returns a table with lead activities. |
| `Marketo.Leads` | Marketo | table |  | Returns a table with lead details. |
| `Marketo.Tables` | Marketo | table |  | Enter the URL of the Marketo REST API endpoint associated with your account. |
| `MarkLogicODBC.Contents` | MarkLogicODBC | table |  | Returns the list of tables returned from the ODBC driver |
| `MicrosoftAzureDataManagerForEnergy.Search` | MicrosoftAzureDataManagerForEnergy | table |  | Queries for records in the Microsoft Azure Data Manager for Energy instance |
| `MicrosoftGraphSecurity.Contents` | MicrosoftGraphSecurity | table |  | Connector for the Microsoft Graph Security API |
| `MicrosoftSentinel.Contents` | MicrosoftSentinel | table |  | Imports data from Sentinel KQL |
| `MicroStrategyDataset.Contents` | MicroStrategyDataset | table |  |  |
| `MicroStrategyDataset.TestConnection` | MicroStrategyDataset | any |  |  |
| `Mixpanel.Contents` | Mixpanel | any |  |  |
| `Mixpanel.Export` | Mixpanel | any |  |  |
| `Mixpanel.FunnelById` | Mixpanel | any |  |  |
| `Mixpanel.FunnelByName` | Mixpanel | any |  |  |
| `Mixpanel.Funnels` | Mixpanel | any |  |  |
| `Mixpanel.Segmentation` | Mixpanel | any |  |  |
| `Mixpanel.Tables` | Mixpanel | any |  |  |
| `MongoDBAtlasODBC.Contents` | MongoDBAtlasODBC | table |  |  |
| `MongoDBAtlasODBC.Query` | MongoDBAtlasODBC | any |  |  |
| `Netezza.Database` | Netezza | table |  | Import data from an IBM Netezza database. |
| `OneLake.Contents` | OneLake | table |  | Access data in OneLake storage |
| `OneLake.SqlAnalytics` | OneLake | table |  | Imports data from Fabric SQL Analytics endpoint |
| `OneStream.Navigation` | OneStream | any |  |  |
| `OpenSearchProject.Contents` | OpenSearchProject | table |  |  |
| `Paxata.Contents` | Paxata | table |  |  |
| `PlanviewEnterprise.CallQueryService` | PlanviewEnterprise | table |  | Enter the URL, database name associated with your Planview Portfolios account and a SQL query. |
| `PlanviewEnterprise.Feed` | PlanviewEnterprise | table |  | Enter the URL and database name associated with your Planview Portfolios account. |
| `PlanviewOKR.Contents` | PlanviewOKR | table |  | Enter the URL of your Planview OKR account. |
| `PlanviewProjectplace.Contents` | PlanviewProjectplace | table |  | Enter the URL of your Planview ProjectPlace account. |
| `PowerBI.Dataflows` | PowerBI | table |  | Connect to all the Power BI dataflows you have access to, and choose the entities you’d like to use. |
| `PowerBI.Datamarts` | PowerBI | table |  | Imports data from Datamarts |
| `PowerPlatform.Dataflows` | PowerPlatform | table |  | Import data from a dataflow |
| `ProductInsights.Contents` | ProductInsights | table |  |  |
| `ProductInsights.QueryMetric` | ProductInsights | any |  |  |
| `Profisee.Tables` | Profisee | table |  | Navigation Table returning Profisee entities. |
| `Projectplace.Feed` | Projectplace | table |  | Enter the URL of your Planview Projectplace account. |
| `Python.Execute` | Python | table |  | Executes Python script and returns data frames |
| `QubolePresto.Contents` | QubolePresto | any |  |  |
| `QuickBase.Contents` | QuickBase | table |  | Quick Base Connector |
| `QuickBooks.Query` | QuickBooks | table |  |  |
| `QuickBooks.Report` | QuickBooks | table |  |  |
| `QuickBooks.Tables` | QuickBooks | any |  |  |
| `R.Execute` | R | table |  |  |
| `Resource.Access` | Resource | any |  | Resource.Access |
| `Roamler.Contents` | Roamler | any |  |  |
| `Samsara.Records` | Samsara | table |  | Get records from supported Samsara APIs |
| `SDMX.Contents` | SDMX | table |  | Get data from an SDMX RESTful web service that supports the CSV format. |
| `ShortcutsBI.Contents` | ShortcutsBI | table |  |  |
| `SingleStoreODBC.Contents` | SingleStoreODBC | table |  | The SingleStore Connector is a high-performance connector that lets you DirectQuery and import data from your SingleSto… |
| `SingleStoreODBC.Database` | SingleStoreODBC | table |  | The SingleStore Connector is a high-performance connector that lets you DirectQuery and import data from your SingleSto… |
| `SingleStoreODBC.DataSource` | SingleStoreODBC | table |  | The SingleStore Connector is a high-performance connector that lets you DirectQuery and import data from your SingleSto… |
| `SingleStoreODBC.Query` | SingleStoreODBC | table |  | The SingleStore Connector is a high-performance connector that lets you DirectQuery and import data from your SingleSto… |
| `Siteimprove.Contents` | Siteimprove | table |  | Siteimprove API connector |
| `Smartsheet.Content` | Smartsheet | any |  | Returns a table of data from an Smartsheet index endpoint. |
| `Smartsheet.Query` | Smartsheet | any |  | Returns a JSON result from the Smartsheet API |
| `Smartsheet.Tables` | Smartsheet | table |  | Returns a table of sheets, reports, folders, and workspaces from the Smartsheet API |
| `SmartsheetGlobal.Contents` | SmartsheetGlobal | table |  | Returns a table of sheets, reports, folders, and workspaces from the Smartsheet API |
| `SmartsheetGlobal.Query` | SmartsheetGlobal | any |  | Returns a JSON result from the Smartsheet API |
| `Snowflake.Databases` | Snowflake | table |  | Import data from a Snowflake Computing warehouse. |
| `SoftOneBI.Contents` | SoftOneBI | table |  | Retrieves all Soft1/Atlantis tables in the datalake |
| `SolarWindsServiceDesk.Contents` | SolarWindsServiceDesk | any |  |  |
| `SolarWindsServiceDesk.ContentsV110` | SolarWindsServiceDesk | any |  |  |
| `SolarWindsServiceDesk.ContentsV113` | SolarWindsServiceDesk | any |  |  |
| `Spark.Tables` | Spark | table |  | Returns a table listing the tables on the specified Spark cluster. |
| `SparkPost.GetList` | SparkPost | table |  | This function can be used to call any of the "Lists" endpoints offered by the SparkPost API v1. |
| `SparkPost.GetTable` | SparkPost | table |  | Returns a table of available metrics from the SparkPost API v1 |
| `SparkPost.NavTable` | SparkPost | table |  | Retrieve the built-in tables exposed by the SparkPost connector with data aggregated over a user-specified number of da… |
| `Spigit.Contents` | Spigit | table |  | Enter the URL of your Planview IdeaPlace account. |
| `StarburstAad.Contents` | StarburstAad | table |  |  |
| `StarburstPresto.Contents` | StarburstPresto | table |  |  |
| `Stripe.Contents` | Stripe | table |  | Makes a call to the Stripe API, with the option to limit number of API calls made. |
| `Stripe.Method` | Stripe | table |  | Makes a call to the Stripe API. |
| `Stripe.Tables` | Stripe | table |  | Returns a table listing the available Stripe tables and functions. |
| `SumTotal.ODataFeed` | SumTotal | table |  | SumTotal's Custom connector connects to SumTotal's external facing OData API service to pull data from data warehousing… |
| `Supermetrics.Render` | Supermetrics | table |  |  |
| `Supermetrics.Test` | Supermetrics | any |  |  |
| `SurveyMonkey.Contents` | SurveyMonkey | table |  | A Navigation table showing all the surveys in the account related to the input access token. |
| `SweetIQ.Contents` | SweetIQ | any |  |  |
| `SweetIQ.Tables` | SweetIQ | any |  |  |
| `Synapse.Contents` | Synapse | table |  | PQ Connector for Azure Synapse Analytics workspace |
| `TeamDesk.Database` | TeamDesk | table |  | Connects to TeamDesk database and let you select a table and a view to retrieve the data from. |
| `TeamDesk.Select` | TeamDesk | table |  | Retrieves the data from select columns in provided table. |
| `TeamDesk.SelectView` | TeamDesk | table |  | Retrieves the data from provided table and view. |
| `TeamsAnalytics.Contents` | TeamsAnalytics | table |  | The Teams Analytics connector enables you to get insights into your usage of Teams. |
| `Tenforce.Contents` | Tenforce | table |  | Selection data |
| `TibcoTdv.DataSource` | TibcoTdv | table |  |  |
| `TimeSeriesInsights.Contents` | TimeSeriesInsights | table |  |  |
| `Troux.CustomFeed` | Troux | table |  | Enter the URL of your Planview Enterprise Architecture account and a query. |
| `Troux.Feed` | Troux | table |  | Enter the URL of your Planview Enterprise Architecture account. |
| `Troux.TestConnection` | Troux | any |  |  |
| `Twilio.Contents` | Twilio | any |  |  |
| `Twilio.Tables` | Twilio | table |  | Enter the number of months of historical Twilio data to retrieve. |
| `Twilio.URL` | Twilio | any |  |  |
| `Usercube.Universes` | Usercube | table |  | Provides data from a Usercube instance |
| `Vena.Contents` | Vena | table |  | Vena |
| `Vertica.Database` | Vertica | table |  | Import data from Vertica |
| `VesselInsight.Contents` | VesselInsight | any |  |  |
| `VivaInsights.Data` | VivaInsights | table |  | Import weekly metrics and attribute data from Workplace Analytics. |
| `VivaInsightsApi.GetResults` | VivaInsightsApi | any |  |  |
| `VSTS.AccountContents` | VSTS | binary |  | Enter Url of your Azure DevOps Analytics Service. |
| `VSTS.AnalyticsViews` | VSTS | table |  | Enter organization and project names. |
| `VSTS.Contents` | VSTS | binary |  | Enter Url of your Azure DevOps Analytics Service. |
| `VSTS.Feed` | VSTS | table |  | Azure DevOps Services Feed |
| `VSTS.Views` | VSTS | table |  | Enter organization and project names. |
| `Webtrends.KeyMetrics` | Webtrends | table |  | Returns a table with key Webtrends metrics. |
| `Webtrends.Profile` | Webtrends | any |  |  |
| `Webtrends.ReportContents` | Webtrends | table |  | Returns a table with report content from Webtrends. |
| `Webtrends.Tables` | Webtrends | table |  | Enter the Profile ID associated with your Webtrends account. |
| `WebtrendsAnalytics.Tables` | WebtrendsAnalytics | table |  | Enter the Profile ID associated with your Webtrends account. |
| `Windsor.Main` | Windsor | table |  |  |
| `Witivio.Contents` | Witivio | table |  | Witivio 365 - Configuration |
| `WorkforceDimensions.Contents` | WorkforceDimensions | text |  | Configuration to access OAuth server as well as default date range settigns. |
| `Wrike.Contents` | Wrike | table |  | Shared function and first entry point to Connector. |
| `Zendesk.Collection` | Zendesk | any |  |  |
| `Zendesk.Tables` | Zendesk | table |  | Enter the URL of your Zendesk account. |
| `ZendeskData.Contents` | ZendeskData | table |  | Returns a table with relevant Zendesk data. |
| `ZohoCreator.Contents` | ZohoCreator | any |  | This connector will fetch data only from Zoho Creator application reports |
| `Zucchetti.Contents` | Zucchetti | table |  | Returns contents of VisualQueries (vqr), reports or functions published by the Zucchetti HR software |
