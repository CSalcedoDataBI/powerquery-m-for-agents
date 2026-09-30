# M constants

201 non-function members of `#shared` (`desktop` 2.157.879.0): enum values, type values and numeric constants. `Value` is the member as text (en-US); empty when it is not a primitive, such as a type, or when it is a machine setting such as `Culture.Current`. ⌂ = not in every host. They have no cards.

| Name | Type | Value | Flags | Summary |
|---|---|---|---|---|
| `AccessControlEntry.ConditionContextType` | type |  |  | The authorization context against which an access control entry (ACE) condition is evaluated. |
| `AccessControlEntry.Type` | type |  |  | A table of access control entries (ACEs). |
| `AccessControlKind.Allow` | number | `1` |  | Access is allowed. |
| `AccessControlKind.Deny` | number | `0` |  | Access is denied. |
| `AccessControlKind.Type` | type |  |  | Specifies the kind of access control. |
| `Any.Type` | type |  |  | The type that represents all values. |
| `Binary.Type` | type |  |  | The type that represents all binary values. |
| `BinaryEncoding.Base64` | number | `0` |  | Constant to use as the encoding type when base-64 encoding is required. |
| `BinaryEncoding.Hex` | number | `1` |  | Constant to use as the encoding type when hexadecimal encoding is required. |
| `BinaryEncoding.Type` | type |  |  | Specifies the type of binary encoding. |
| `BinaryOccurrence.Optional` | number | `0` |  | The item is expected to appear zero or one time in the input. |
| `BinaryOccurrence.Repeating` | number | `2` |  | The item is expected to appear zero or more times in the input. |
| `BinaryOccurrence.Required` | number | `1` |  | The item is expected to appear once in the input. |
| `BinaryOccurrence.Type` | type |  |  | Specifies how many times the item is expected to appear in the group. |
| `BufferMode.Delayed` | number | `2` |  | The type of the value is computed immediately but its contents aren't buffered until data is needed, at which point the entire value is immediately buffered. |
| `BufferMode.Eager` | number | `1` |  | The entire value is immediately buffered in memory before continuing. |
| `BufferMode.Type` | type |  |  | Describes the type of buffering to be performed. |
| `Byte.Type` | type |  |  | The type that represents all bytes. |
| `ByteOrder.BigEndian` | number | `1` |  | A possible value for the `byteOrder` parameter in `BinaryFormat.ByteOrder`. The most significant byte appears first in Big Endian byte order. |
| `ByteOrder.LittleEndian` | number | `0` |  | A possible value for the `byteOrder` parameter in `BinaryFormat.ByteOrder`. The least significant byte appears first in Little Endian byte order. |
| `ByteOrder.Type` | type |  |  | Specifies the byte order. |
| `Certificate.Type` | type |  |  | The type that represents a pkcs8 Certificate Text. |
| `Character.Type` | type |  |  | The type that represents all characters. |
| `Compression.Brotli` | number | `3` |  | The compressed data is in the 'Brotli' format. |
| `Compression.Deflate` | number | `1` |  | The compressed data is in the 'Deflate' format. |
| `Compression.GZip` | number | `0` |  | The compressed data is in the 'GZip' format. |
| `Compression.LZ4` | number | `4` |  | The compressed data is in the 'LZ4' format. |
| `Compression.None` | number | `-1` |  | The data is uncompressed. |
| `Compression.Snappy` | number | `2` |  | The compressed data is in the 'Snappy' format. |
| `Compression.Type` | type |  |  | Specifies the type of compression. |
| `Compression.Zstandard` | number | `5` |  | The compressed data is in the 'Zstandard' format. |
| `CsvStyle.QuoteAfterDelimiter` | number | `0` |  | Quotes in a field are only significant immediately following the delimiter. |
| `CsvStyle.QuoteAlways` | number | `1` |  | Quotes in a field are always significant regardless of where they appear. |
| `CsvStyle.Type` | type |  |  | Specifies the significance of quotes in CSV documents. |
| `Culture.Current` | text |  |  | Returns the name of the current culture for the application. |
| `Currency.Type` | type |  |  | The type that represents currency value. |
| `Date.Type` | type |  |  | The type that represents all date values. |
| `DateTime.Type` | type |  |  | The type that represents all date and time values without an associated timezone. |
| `DateTimeZone.Type` | type |  |  | The type that represents all date and time values relative to a timezone. |
| `Day.Friday` | number | `5` |  | Represents Friday. |
| `Day.Monday` | number | `1` |  | Represents Monday. |
| `Day.Saturday` | number | `6` |  | Represents Saturday. |
| `Day.Sunday` | number | `0` |  | Represents Sunday. |
| `Day.Thursday` | number | `4` |  | Represents Thursday. |
| `Day.Tuesday` | number | `2` |  | Represents Tuesday. |
| `Day.Type` | type |  |  | Specifies a day of week. |
| `Day.Wednesday` | number | `3` |  | Represents Wednesday. |
| `Decimal.Type` | type |  |  | The type that represents fixed-point decimal number. |
| `Double.Type` | type |  |  | The type that represents double precision floating point number. |
| `Duration.Type` | type |  |  | The type that represents all duration values |
| `EmigoDataSourceConnector.NavigationFunctionType` | type |  |  |  |
| `Excel.RichDocument` | null |  |  |  |
| `ExtraValues.Error` | number | `1` |  | If the splitter function returns more columns than the table expects, an error should be raised. |
| `ExtraValues.Ignore` | number | `2` |  | If the splitter function returns more columns than the table expects, they should be ignored. |
| `ExtraValues.List` | number | `0` |  | If the splitter function returns more columns than the table expects, they should be collected into a list. |
| `ExtraValues.Type` | type |  |  | Specifies the expected action for extra values in a row that contains columns more than expected. |
| `Function.Type` | type |  |  | The type that represents all functions. |
| `GroupKind.Global` | number | `1` |  | A global group is formed from all rows in an input table with the same key value. Note that only a single global group is produced for a given key value. |
| `GroupKind.Local` | number | `0` |  | A local group is formed from a consecutive sequence of rows from an input table with the same key value. Note that multiple local groups may be produced with the same key value. |
| `GroupKind.Type` | type |  |  | Specifies the kind of grouping. |
| `Guid.Type` | type |  |  | The type that represents a Guid value. |
| `HiveProtocol.HTTP` | number | `2` |  |  |
| `HiveProtocol.Standard` | number | `1` |  |  |
| `HiveProtocol.Type` | type |  |  | HiveProtocolEnum |
| `Identity.Type` | type |  |  | An identity represents a user, group, device, or other identifiable thing. |
| `IdentityProvider.Type` | type |  |  | Defines a scope in which identities are created and compared. |
| `Int16.Type` | type |  |  | The type that represents signed 16 bit integer. |
| `Int32.Type` | type |  |  | The type that represents signed 32 bit integer. |
| `Int64.Type` | type |  |  | The type that represents signed 64 bit integer. |
| `Int8.Type` | type |  |  | The type that represents signed 8 bit integer. |
| `ItemExpression.Item` | record |  |  | An abstract syntax tree (AST) node representing the item in an item expression. |
| `JoinAlgorithm.Dynamic` | number | `0` |  | Automatically chooses a join algorithm based on inspecting the initial rows and metadata of both tables. |
| `JoinAlgorithm.LeftHash` | number | `3` |  | Buffers the left rows into a lookup table and streams the right rows. For each right row, the matching left rows are found via the buffered lookup table. This algorithm is recommended when the left t… |
| `JoinAlgorithm.LeftIndex` | number | `5` |  | In batches, uses the keys from the left table to do predicate-based queries against the right table. This algorithm is recommended when the right table is large, supports folding of Table.SelectRows,… |
| `JoinAlgorithm.PairwiseHash` | number | `1` |  | Buffers the rows of both the left and right tables until one of the tables is completely buffered, and then performs a LeftHash or RightHash, depending on which table was buffered completely. This al… |
| `JoinAlgorithm.RightHash` | number | `4` |  | Buffers the right rows into a lookup table and streams the left rows. For each left row, the matching right rows are found via the buffered lookup table. This algorithm is recommended when the right… |
| `JoinAlgorithm.RightIndex` | number | `6` |  | In batches, uses the keys from the right table to do predicate-based queries against the left table. This algorithm is recommended when the left table is large, supports folding of Table.SelectRows,… |
| `JoinAlgorithm.SortMerge` | number | `2` |  | Performs a streaming merge based on the assumption that both tables are sorted by their join keys. While efficient, it will return incorrect results if the tables aren't sorted as expected. |
| `JoinAlgorithm.Type` | type |  |  | Specifies the join algorithm to be used in the join operation. |
| `JoinKind.FullOuter` | number | `3` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A full outer join ensures that all rows of both tables appear in the result. Rows that did not have a match in the other table… |
| `JoinKind.Inner` | number | `0` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. The table resulting from an inner join contains a row for each pair of rows from the specified tables that were determined to m… |
| `JoinKind.LeftAnti` | number | `4` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A left anti join returns all rows from the first table that do not have a match in the second table. |
| `JoinKind.LeftOuter` | number | `1` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A left outer join ensures that all rows of the first table appear in the result. |
| `JoinKind.LeftSemi` | number | `6` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A left semi join returns all rows from the first table that have a match in the second table. |
| `JoinKind.RightAnti` | number | `5` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A right anti join returns all rows from the second table that do not have a match in the first table. |
| `JoinKind.RightOuter` | number | `2` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A right outer join ensures that all rows of the second table appear in the result. |
| `JoinKind.RightSemi` | number | `7` |  | A possible value for the optional `JoinKind` parameter in `Table.Join`. A right semi join returns all rows from the second table that have a match in the first table. |
| `JoinKind.Type` | type |  |  | Specifies the kind of join operation. |
| `JoinSide.Left` | number | `0` |  | Specifies the left table of a join. |
| `JoinSide.Right` | number | `1` |  | Specifies the right table of a join. |
| `JoinSide.Type` | type |  |  | Specifies the left or right table of a join. |
| `LimitClauseKind.AnsiSql2008` | number | `4` |  | This SQL dialect supports an ANSI SQL-compatible LIMIT N ROWS specifier to limit the number of rows returned. |
| `LimitClauseKind.Limit` | number | `3` |  | This SQL dialect supports a LIMIT specifier to limit the number of rows returned. |
| `LimitClauseKind.LimitOffset` | number | `2` |  | This SQL dialect supports LIMIT and OFFSET specifiers to limit the number of rows returned. |
| `LimitClauseKind.None` | number | `0` |  | This SQL dialect does not support a limit clause. |
| `LimitClauseKind.Top` | number | `1` |  | This SQL dialect supports a TOP specifier to limit the number of rows returned. |
| `LimitClauseKind.Type` | type |  |  | Describes the type of limit clause supported by the SQL dialect used by this data source. |
| `List.Type` | type |  |  | The type that represents all lists. |
| `Logical.Type` | type |  |  | The type that represents all logical values. |
| `MissingField.Error` | number | `0` |  | Indicates that missing fields should result in an error. (This is the default value.) |
| `MissingField.Ignore` | number | `1` |  | Indicates that missing fields should be ignored. |
| `MissingField.Type` | type |  |  | Specifies the expected action for missing values in a row that contains columns less than expected. |
| `MissingField.UseNull` | number | `2` |  | Indicates that missing fields should be included as null values. |
| `None.Type` | type |  |  | None.Type |
| `Null.Type` | type |  |  | The type that represents null. |
| `Number.E` | number | `2.7182818284590451` |  | A constant value that represents e. |
| `Number.Epsilon` | number | `4.94065645841247E-324` |  | A constant value that represents the smallest positive number a floating-point number can hold. |
| `Number.NaN` | number | `NaN` |  | A constant value that represents 0 divided by 0. |
| `Number.NegativeInfinity` | number | `-∞` |  | A constant value that represents -1 divided by 0. |
| `Number.PI` | number | `3.1415926535897931` |  | A constant that represents pi. |
| `Number.PositiveInfinity` | number | `∞` |  | A constant value that represents 1 divided by 0. |
| `Number.Type` | type |  |  | The type that represents all numbers. |
| `Occurrence.All` | number | `2` |  | A list of positions of all occurrences of the found values is returned. |
| `Occurrence.First` | number | `0` |  | The position of the first occurrence of the found value is returned. |
| `Occurrence.Last` | number | `1` |  | The position of the last occurrence of the found value is returned. |
| `Occurrence.Optional` | number | `0` |  | The item is expected to appear zero or one time in the input. |
| `Occurrence.Repeating` | number | `2` |  | The item is expected to appear zero or more times in the input. |
| `Occurrence.Required` | number | `1` |  | The item is expected to appear once in the input. |
| `Occurrence.Type` | type |  |  | Specifies the occurrence of an element in a sequence. |
| `ODataOmitValues.Nulls` | text | `nulls` |  | Allows the OData service to omit null values. |
| `ODataOmitValues.Type` | type |  |  | Specifies the kinds of values an OData service can omit. |
| `Office.InferChartPropertiesGenerator` | null |  |  |  |
| `Order.Ascending` | number | `0` |  | Sorts the values in ascending order. |
| `Order.Descending` | number | `1` |  | Sorts the values in descending order. |
| `Order.Type` | type |  |  | Specifies the direction of sorting. |
| `Password.Type` | type |  |  | The type that represents a text password. |
| `Percentage.Type` | type |  |  | The type that represents percentage value. |
| `PercentileMode.ExcelExc` | number | `2` |  | When interpolating values for `List.Percentile`, use a method compatible with Excel's `PERCENTILE.EXC`. |
| `PercentileMode.ExcelInc` | number | `1` |  | When interpolating values for `List.Percentile`, use a method compatible with Excel's `PERCENTILE.INC`. |
| `PercentileMode.SqlCont` | number | `4` |  | When interpolating values for `List.Percentile`, use a method compatible with SQL Server's `PERCENTILE_CONT`. |
| `PercentileMode.SqlDisc` | number | `3` |  | When interpolating values for `List.Percentile`, use a method compatible with SQL Server's `PERCENTILE_DISC`. |
| `PercentileMode.Type` | type |  |  | Specifies the percentile mode type. |
| `PowerPoint.Presentation` | null |  |  |  |
| `Precision.Decimal` | number | `1` |  | An optional parameter for the built-in arithmetic operators to specify decimal precision. |
| `Precision.Double` | number | `0` |  | An optional parameter for the built-in arithmetic operators to specify double precision. |
| `Precision.Type` | type |  |  | Specifies the precision of comparison. |
| `QuoteStyle.Csv` | number | `1` |  | Quote characters indicate the start of a quoted string. Nested quotes are indicated by two quote characters. |
| `QuoteStyle.None` | number | `0` |  | Quote characters have no significance. |
| `QuoteStyle.Type` | type |  |  | Specifies the quote style. |
| `RankKind.Competition` | number | `0` |  | Items which compare as equal receive the same ranking number and then a gap is left before the next ranking. |
| `RankKind.Dense` | number | `1` |  | Items which compare as equal receive the same ranking number and the next item is numbered consecutively with no gap. |
| `RankKind.Ordinal` | number | `2` |  | All items are given a unique ranking number even if they compare as equal. |
| `RankKind.Type` | type |  |  | Specifies the type of ranking. |
| `Record.Type` | type |  |  | The type that represents all records. |
| `RelativePosition.FromEnd` | number | `1` |  | Indicates indexing should be done from the end of the input. |
| `RelativePosition.FromStart` | number | `0` |  | Indicates indexing should be done from the start of the input. |
| `RelativePosition.Type` | type |  |  | Indicates whether indexing should be done from the start or end of the input. |
| `RoundingMode.AwayFromZero` | number | `2` |  | Round away from zero when there is a tie between the possible numbers to round to. |
| `RoundingMode.Down` | number | `1` |  | Round down when there is a tie between the possible numbers to round to. |
| `RoundingMode.ToEven` | number | `4` |  | Round to the nearest even number when there is a tie between the possible numbers to round to. |
| `RoundingMode.TowardZero` | number | `3` |  | Round toward zero when there is a tie between the possible numbers to round to. |
| `RoundingMode.Type` | type |  |  | Specifies rounding direction when there is a tie between the possible numbers to round to. |
| `RoundingMode.Up` | number | `0` |  | Round up when there is a tie between the possible numbers to round to. |
| `RowExpression.Row` | record |  |  | An abstract syntax tree (AST) node representing the row in a row expression. |
| `SapBusinessWarehouseExecutionMode.BasXml` | number | `64` |  | 'bXML flattening mode' option for MDX execution in SAP Business Warehouse. |
| `SapBusinessWarehouseExecutionMode.BasXmlGzip` | number | `65` |  | 'Gzip compressed bXML flattening mode' option for MDX execution in SAP Business Warehouse. Recommended for low latency or high volume queries. |
| `SapBusinessWarehouseExecutionMode.DataStream` | number | `66` |  | 'DataStream flattening mode' option for MDX execution in SAP Business Warehouse. |
| `SapBusinessWarehouseExecutionMode.Type` | type |  |  | Valid options for SAP Business Warehouse execution mode option. |
| `SapHanaDistribution.All` | number | `3` |  | 'All' distribution option for SAP HANA. |
| `SapHanaDistribution.Connection` | number | `1` |  | 'Connection' distribution option for SAP HANA. |
| `SapHanaDistribution.Off` | number | `0` |  | 'Off' distribution option for SAP HANA. |
| `SapHanaDistribution.Statement` | number | `2` |  | 'Statement' distribution option for SAP HANA. |
| `SapHanaDistribution.Type` | type |  |  | Valid options for SAP HANA distribution option. |
| `SapHanaRangeOperator.Equals` | number | `4` |  | 'Equals' range operator for SAP HANA input parameters. |
| `SapHanaRangeOperator.GreaterThan` | number | `0` |  | 'Greater than' range operator for SAP HANA input parameters. |
| `SapHanaRangeOperator.GreaterThanOrEquals` | number | `2` |  | 'Greater than or equals' range operator for SAP HANA input parameters. |
| `SapHanaRangeOperator.LessThan` | number | `1` |  | 'Less than' range operator for SAP HANA input parameters. |
| `SapHanaRangeOperator.LessThanOrEquals` | number | `3` |  | 'Less than or equals' range operator for SAP HANA input parameters. |
| `SapHanaRangeOperator.NotEquals` | number | `5` |  | 'Not equals' range operator for SAP HANA input parameters. |
| `SapHanaRangeOperator.Type` | type |  |  | A range operator for SAP HANA range input parameters. |
| `Single.Type` | type |  |  | The type that represents single precision floating point number. |
| `SparkProtocol.Azure` | number | `1` |  |  |
| `SparkProtocol.HTTP` | number | `2` |  |  |
| `SparkProtocol.Standard` | number | `0` |  |  |
| `SparkProtocol.Type` | type |  |  | The protocol to use when connecting to an instance of Spark. |
| `Table.Type` | type |  |  | The type that represents all tables. |
| `Text.Type` | type |  |  | The type that represents all text values. |
| `TextEncoding.Ascii` | number | `20127` |  | Use to choose the ASCII binary form. |
| `TextEncoding.BigEndianUnicode` | number | `1201` |  | Use to choose the UTF16 big endian binary form. |
| `TextEncoding.Type` | type |  |  | Specifies the text encoding type. |
| `TextEncoding.Unicode` | number | `1200` |  | Use to choose the UTF16 little endian binary form. |
| `TextEncoding.Utf16` | number | `1200` |  | Use to choose the UTF16 little endian binary form. |
| `TextEncoding.Utf8` | number | `65001` |  | Use to choose the UTF8 binary form. |
| `TextEncoding.Windows` | number | `1252` |  | Use to choose the Windows binary form. |
| `Time.Type` | type |  |  | The type that represents all time values. |
| `TimeZone.Current` | text |  |  | Returns the name of the current time zone for the application. |
| `TraceLevel.Critical` | number | `1` |  | Specifies Critical trace level. |
| `TraceLevel.Error` | number | `2` |  | Specifies Error trace level. |
| `TraceLevel.Information` | number | `8` |  | Specifies Information trace level. |
| `TraceLevel.Type` | type |  |  | Specifies the trace level. |
| `TraceLevel.Verbose` | number | `16` |  | Specifies Verbose trace level. |
| `TraceLevel.Warning` | number | `4` |  | Specifies Warning trace level. |
| `Type.Type` | type |  |  | The type that represents all types. |
| `Uri.Type` | type |  |  | The type that represents a text URI. |
| `WebMethod.Delete` | text | `DELETE` |  | Specifies the DELETE method for HTTP. |
| `WebMethod.Get` | text | `GET` |  | Specifies the GET method for HTTP. |
| `WebMethod.Head` | text | `HEAD` |  | Specifies the HEAD method for HTTP. |
| `WebMethod.Patch` | text | `PATCH` |  | Specifies the PATCH method for HTTP. |
| `WebMethod.Post` | text | `POST` |  | Specifies the POST method for HTTP. |
| `WebMethod.Put` | text | `PUT` |  | Specifies the PUT method for HTTP. |
| `WebMethod.Type` | type |  |  | Specifies an HTTP method. |
