# M function catalogue

659 library functions from `#shared` (`desktop` 2.157.879.0). Flags: ★ field note · ▶ executed examples · ⌂ not in every host.
Not listed here: 273 connector entry points are in `connectors.md`; 201 constants and type values in `constants.md`.
Open one card: `library/<file>.md`, where <file> is the name in lower case with every run of non-alphanumerics as one dash (`Table.AddColumn` -> `table-addcolumn`).

| Function | Category | Returns | Flags | Summary |
|---|---|---|---|---|
| `Access.Database` | Accessing data | table |  | Returns a structural representation of an Access database. |
| `AccessControlEntry.ConditionToIdentities` | Accessing data | list |  | Returns a list of identities that the condition will accept. |
| `Action.WithErrorContext` | Values.Implementation | any |  | This function is intended for internal use only. |
| `ActiveDirectory.Domains` | Accessing data | table |  | Returns a list of Active Directory domains in the same forest as the specified domain or of the current machine's domai… |
| `AdobeAnalytics.Cubes` | Accessing data | table |  | Returns the report suites in Adobe Analytics. |
| `AdoDotNet.DataSource` | Accessing data | table |  | Returns the schema collection for an ADO.NET data source. |
| `AdoDotNet.Query` | Accessing data | table |  | Returns the result of running a native query on an ADO.NET data source. |
| `AnalysisServices.Database` | Accessing data | table |  | Returns a table of multidimensional cubes or tabular models from the Analysis Services database. |
| `AnalysisServices.Databases` | Accessing data | table |  | Returns the Analysis Services databases on a particular host. |
| `AzureStorage.BlobContents` | Accessing data | binary |  | Returns the content of the specified blob from an Azure storage vault. |
| `AzureStorage.Blobs` | Accessing data | table |  | Returns a navigational table containing the containers found in the specified account from an Azure storage vault. |
| `AzureStorage.DataLake` | Accessing data | table |  | Returns a navigational table containing the documents found in the specified container and its subfolders from Azure Da… |
| `AzureStorage.DataLakeContents` | Accessing data | binary |  | Returns the content of the specified file from an Azure Data Lake Storage filesystem. |
| `AzureStorage.Tables` | Accessing data | table |  | Returns a navigational table containing the tables found in the specified account from an Azure storage vault. |
| `Binary.ApproximateLength` | Binary | nullable number | ▶ | Returns the approximate length of the binary. |
| `Binary.Buffer` | Binary | nullable binary | ▶ | Buffers the binary value in memory. |
| `Binary.Combine` | Binary | binary | ▶ | Combines a list of binaries into a single binary. |
| `Binary.Compress` | Binary | nullable binary | ▶ | Compresses a binary value using the given compression type. |
| `Binary.Decompress` | Binary | nullable binary | ▶ | Decompresses a binary value using the given compression type. |
| `Binary.From` | Binary | nullable binary | ▶ | Creates a binary from the given value |
| `Binary.FromList` | Binary | binary | ▶ | Converts a list of numbers into a binary value. |
| `Binary.FromText` | Binary | nullable binary | ▶ | Decodes data from a text form into binary. |
| `Binary.InferContentType` | Binary | record | ▶ | Reads the binary stream and tries to determine the content type and format information of the stream. |
| `Binary.Length` | Binary | nullable number | ▶ | Returns the number of characters. |
| `Binary.Range` | Binary | binary | ▶ | Returns a subset of the binary value beginning at an offset. |
| `Binary.Split` | Binary | list | ▶ | Splits the specified binary into a list of binaries using the specified page size. |
| `Binary.ToList` | Binary | list | ▶ | Converts a binary value into a list of numbers. |
| `Binary.ToText` | Binary | nullable text | ▶ | Encodes binary data into a text form. |
| `Binary.View` | Binary | binary | ▶ | Creates or extends a binary with user-defined handlers for query and action operations. |
| `Binary.ViewError` | Binary | record | ▶ | Creates a modified error record which won't trigger a fallback when raised by a handler defined on a view (via Binary.V… |
| `Binary.ViewFunction` | Binary | function | ▶ | Creates a function that can be intercepted by a handler defined on a view (via Binary.View). |
| `BinaryFormat.7BitEncodedSignedInteger` | Binary Formats.Reading numbers | any |  | A binary format that reads a 64-bit signed integer that was encoded using a 7-bit variable-length encoding. |
| `BinaryFormat.7BitEncodedUnsignedInteger` | Binary Formats.Reading numbers | any |  | A binary format that reads a 64-bit unsigned integer that was encoded using a 7-bit variable-length encoding. |
| `BinaryFormat.Binary` | Binary Formats.Reading binary data | function |  | Returns a binary format that reads a binary value. |
| `BinaryFormat.Byte` | Binary Formats.Reading numbers | any |  | A binary format that reads an 8-bit unsigned integer. |
| `BinaryFormat.ByteOrder` | Binary Formats.Controlling byte order | function |  | Returns a binary format with the byte order specified by a function. |
| `BinaryFormat.Choice` | Binary Formats.Controlling what comes next | function |  | Returns a binary format that chooses the next binary format based on a value that has already been read. |
| `BinaryFormat.Decimal` | Binary Formats.Reading numbers | any |  | A binary format that reads a .NET 16-byte decimal value. |
| `BinaryFormat.Double` | Binary Formats.Reading numbers | any |  | A binary format that reads an 8-byte IEEE double-precision floating point value. |
| `BinaryFormat.Group` | Binary Formats.Reading a group of items | function |  | Returns a binary format that reads a group of items. |
| `BinaryFormat.Length` | Binary Formats.Limiting input | function |  | Returns a binary format that limits the amount of data that can be read. |
| `BinaryFormat.List` | Binary Formats.Reading lists | function |  | Returns a binary format that reads a sequence of items and returns a list. |
| `BinaryFormat.Null` | Binary Formats.Controlling what comes next | any |  | A binary format that reads zero bytes and returns null. |
| `BinaryFormat.Record` | Binary Formats.Reading records | function |  | Returns a binary format that reads a record. |
| `BinaryFormat.SignedInteger16` | Binary Formats.Reading numbers | any |  | A binary format that reads a 16-bit signed integer. |
| `BinaryFormat.SignedInteger32` | Binary Formats.Reading numbers | any |  | A binary format that reads a 32-bit signed integer. |
| `BinaryFormat.SignedInteger64` | Binary Formats.Reading numbers | any |  | A binary format that reads a 64-bit signed integer. |
| `BinaryFormat.Single` | Binary Formats.Reading numbers | any |  | A binary format that reads a 4-byte IEEE single-precision floating point value. |
| `BinaryFormat.Text` | Binary Formats.Reading text | function |  | Returns a binary format that reads a text value. |
| `BinaryFormat.Transform` | Binary Formats.Transforming what was read | function |  | Returns a binary format that will transform the values read by another binary format. |
| `BinaryFormat.UnsignedInteger16` | Binary Formats.Reading numbers | any |  | A binary format that reads a 16-bit unsigned integer. |
| `BinaryFormat.UnsignedInteger32` | Binary Formats.Reading numbers | any |  | A binary format that reads a 32-bit unsigned integer. |
| `BinaryFormat.UnsignedInteger64` | Binary Formats.Reading numbers | any |  | A binary format that reads a 64-bit unsigned integer. |
| `Byte.From` | Number.Conversion and formatting | nullable number | ▶ | Creates an 8-bit integer from the given value. |
| `Cdm.Contents` | Accessing data | table |  | Cdm.Contents |
| `Cdm.MapToEntity` | Cdm | table |  | Returns a table with columns mapped to the attributes of an entity in the Common Data Model, including data types. |
| `Character.FromNumber` | Text.Conversions from and to text | nullable text |  | Converts a number to a text character. |
| `Character.ToNumber` | Text.Conversions from and to text | nullable number |  | Converts a character to a number value. |
| `Combiner.CombineTextByDelimiter` | Combiner | function |  | Returns a function that combines a list of text using the specified delimiter. |
| `Combiner.CombineTextByEachDelimiter` | Combiner | function |  | Returns a function that combines a list of text using a sequence of delimiters. |
| `Combiner.CombineTextByLengths` | Combiner | function |  | Returns a function that combines a list of text using the specified lengths. |
| `Combiner.CombineTextByPositions` | Combiner | function |  | Returns a function that combines a list of text using the specified output positions. |
| `Combiner.CombineTextByRanges` | Combiner | function |  | Returns a function that combines a list of text using the specified positions and lengths. |
| `Comparer.Equals` | Comparer | logical |  | Returns a logical value based on the equality check over the two given values. |
| `Comparer.FromCulture` | Comparer | function |  | Returns a comparer function based on the specified culture and case-sensitivity. |
| `Comparer.Ordinal` | Comparer | number |  | Returns a comparer function which uses Ordinal rules to compare values. |
| `Comparer.OrdinalIgnoreCase` | Comparer | number |  | Returns a case-insensitive comparer function which uses Ordinal rules to compare values. |
| `Csv.Document` | Accessing data | table |  | Returns the contents of the CSV document as a table. |
| `Cube.AddAndExpandDimensionColumn` | Cube | table |  | Merges the specified dimension table into the cube's filter context and changes the dimensional granularity of the filt… |
| `Cube.AddMeasureColumn` | Cube | table |  | Adds a column to the cube that contains the results of the measure applied in the row context of each row. |
| `Cube.ApplyParameter` | Cube | table |  | Returns a cube after applying a parameter to it. |
| `Cube.AttributeMemberId` | Cube | any |  | Returns the unique member identifier from members property value. |
| `Cube.AttributeMemberProperty` | Cube | any |  | Returns a property of a dimension attribute. |
| `Cube.CollapseAndRemoveColumns` | Cube | table |  | Changes the dimensional granularity of the filter context for the cube by collapsing the attributes mapped to the speci… |
| `Cube.Dimensions` | Cube | table |  | Returns a table containing the set of available dimensions. |
| `Cube.DisplayFolders` | Cube | table |  | Returns a nested tree of tables representing the display folder hierarchy of the objects (for example, dimensions and m… |
| `Cube.MeasureProperties` | Cube | table |  | Returns a table containing the set of available measure properties that are expanded in the cube. |
| `Cube.MeasureProperty` | Cube | any |  | Returns a property of a measure (cell property). |
| `Cube.Measures` | Cube | table |  | Returns a table containing the set of available measures. |
| `Cube.Parameters` | Cube | table |  | Returns a table containing the set of parameters that can be applied to the cube. |
| `Cube.Properties` | Cube | table |  | Returns a table containing the set of available properties for dimensions that are expanded in the cube. |
| `Cube.PropertyKey` | Cube | any |  | Returns the key of a property. |
| `Cube.ReplaceDimensions` | Cube | table |  | Replaces the set of dimensions returned by Cube.Dimensions. |
| `Cube.Transform` | Cube | table |  | Applies a list of cube functions. |
| `Currency.From` | Number.Conversion and formatting | nullable number | ▶ | Returns a currency value from the given value. |
| `Date.AddDays` | Date | any | ▶ | Adds the specified days to the date. |
| `Date.AddMonths` | Date | any | ▶ | Adds the specified months to the date. |
| `Date.AddQuarters` | Date | any | ▶ | Adds the specified quarters to the date. |
| `Date.AddWeeks` | Date | any | ▶ | Adds the specified weeks to the date. |
| `Date.AddYears` | Date | any | ▶ | Adds the specified years to the date. |
| `Date.Day` | Date | nullable number | ▶ | Returns the day component. |
| `Date.DayOfWeek` | Date | nullable number | ▶ | Returns a number (from 0 to 6) indicating the day of the week of the provided value. |
| `Date.DayOfWeekName` | Date | nullable text | ▶ | Returns the day of the week name. |
| `Date.DayOfYear` | Date | nullable number | ▶ | Returns a number from 1 to 366 representing the day of the year. |
| `Date.DaysInMonth` | Date | nullable number | ▶ | Returns a number from 28 to 31 indicating the number of days in the month. |
| `Date.EndOfDay` | Date | any | ▶ | Returns the end of the day. |
| `Date.EndOfMonth` | Date | any | ▶ | Returns the end of the month. |
| `Date.EndOfQuarter` | Date | any | ▶ | Returns the end of the quarter. |
| `Date.EndOfWeek` | Date | any | ▶ | Returns the end of the week. |
| `Date.EndOfYear` | Date | any | ▶ | Returns the end of the year. |
| `Date.From` | Date | nullable date | ▶ | Creates a date from the given value. |
| `Date.FromText` | Date | nullable date | ▶ | Creates a Date from local, universal, and custom Date formats. |
| `Date.IsInCurrentDay` | Date | nullable logical | ▶ | Indicates whether this date occurs during the current day, as determined by the current date and time on the system. |
| `Date.IsInCurrentMonth` | Date | nullable logical | ▶ | Indicates whether this date occurs during the current month, as determined by the current date and time on the system. |
| `Date.IsInCurrentQuarter` | Date | nullable logical | ▶ | Indicates whether this date occurs during the current quarter, as determined by the current date and time on the system. |
| `Date.IsInCurrentWeek` | Date | nullable logical | ▶ | Indicates whether this date occurs during the current week, as determined by the current date and time on the system. |
| `Date.IsInCurrentYear` | Date | nullable logical | ▶ | Indicates whether this date occurs during the current year, as determined by the current date and time on the system. |
| `Date.IsInNextDay` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next day, as determined by the current date and time on the system. |
| `Date.IsInNextMonth` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next month, as determined by the current date and time on the system. |
| `Date.IsInNextNDays` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next number of days, as determined by the current date and time on the sy… |
| `Date.IsInNextNMonths` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next number of months, as determined by the current date and time on the… |
| `Date.IsInNextNQuarters` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next number of quarters, as determined by the current date and time on th… |
| `Date.IsInNextNWeeks` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next number of weeks, as determined by the current date and time on the s… |
| `Date.IsInNextNYears` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next number of years, as determined by the current date and time on the s… |
| `Date.IsInNextQuarter` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next quarter, as determined by the current date and time on the system. |
| `Date.IsInNextWeek` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next week, as determined by the current date and time on the system. |
| `Date.IsInNextYear` | Date | nullable logical | ▶ | Indicates whether this date occurs during the next year, as determined by the current date and time on the system. |
| `Date.IsInPreviousDay` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous day, as determined by the current date and time on the system. |
| `Date.IsInPreviousMonth` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous month, as determined by the current date and time on the system. |
| `Date.IsInPreviousNDays` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous number of days, as determined by the current date and time on th… |
| `Date.IsInPreviousNMonths` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous number of months, as determined by the current date and time on… |
| `Date.IsInPreviousNQuarters` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous number of quarters, as determined by the current date and time o… |
| `Date.IsInPreviousNWeeks` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous number of weeks, as determined by the current date and time on t… |
| `Date.IsInPreviousNYears` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous number of years, as determined by the current date and time on t… |
| `Date.IsInPreviousQuarter` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous quarter, as determined by the current date and time on the syste… |
| `Date.IsInPreviousWeek` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous week, as determined by the current date and time on the system. |
| `Date.IsInPreviousYear` | Date | nullable logical | ▶ | Indicates whether this date occurs during the previous year, as determined by the current date and time on the system. |
| `Date.IsInYearToDate` | Date | nullable logical | ▶ | Indicates whether this date occurs during the current year and is on or before the current day, as determined by the cu… |
| `Date.IsLeapYear` | Date | nullable logical | ▶ | Indicates whether this date falls in a leap year. |
| `Date.Month` | Date | nullable number | ▶ | Returns the month component. |
| `Date.MonthName` | Date | nullable text | ▶ | Returns the name of the month component. |
| `Date.QuarterOfYear` | Date | nullable number | ▶ | Returns a number indicating which quarter of the year the date falls in. |
| `Date.StartOfDay` | Date | any | ▶ | Returns the start of the day. |
| `Date.StartOfMonth` | Date | any | ▶ | Returns the start of the month. |
| `Date.StartOfQuarter` | Date | any | ▶ | Returns the start of the quarter. |
| `Date.StartOfWeek` | Date | any | ▶ | Returns the start of the week. |
| `Date.StartOfYear` | Date | any | ▶ | Returns the start of the year. |
| `Date.ToRecord` | Date | record | ▶ | Returns a record containing parts of the date value. |
| `Date.ToText` | Date | nullable text | ▶ | Returns a textual representation of the date value. |
| `Date.WeekOfMonth` | Date | nullable number | ▶ | Returns a number from 1 to 6 indicating which week of the month this date falls in. |
| `Date.WeekOfYear` | Date | nullable number | ▶ | Returns a number from 1 to 54 indicating which week of the year this date falls in. |
| `Date.Year` | Date | nullable number | ▶ | Returns the year component. |
| `DateTime.AddZone` | DateTime | nullable datetimezone | ▶ | Adds timezone information to the datetime value. |
| `DateTime.Date` | DateTime | nullable date | ▶ | Returns the date component of the given date, datetime, or datetimezone value. |
| `DateTime.FixedLocalNow` | DateTime | datetime |  | Returns the current date and time in the local timezone. |
| `DateTime.From` | DateTime | nullable datetime | ▶ | Creates a datetime from the given value. |
| `DateTime.FromFileTime` | DateTime | nullable datetime |  | Creates a datetime from a 64 bits long number. |
| `DateTime.FromText` | DateTime | nullable datetime | ▶ | Creates a datetimezone from local and universal datetime formats. |
| `DateTime.IsInCurrentHour` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the current hour, as determined by the current date and time on the syste… |
| `DateTime.IsInCurrentMinute` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the current minute, as determined by the current date and time on the sys… |
| `DateTime.IsInCurrentSecond` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the current second, as determined by the current date and time on the sys… |
| `DateTime.IsInNextHour` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the next hour, as determined by the current date and time on the system. |
| `DateTime.IsInNextMinute` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the next minute, as determined by the current date and time on the system. |
| `DateTime.IsInNextNHours` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the next number of hours, as determined by the current date and time on t… |
| `DateTime.IsInNextNMinutes` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the next number of minutes, as determined by the current date and time on… |
| `DateTime.IsInNextNSeconds` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the next number of seconds, as determined by the current date and time on… |
| `DateTime.IsInNextSecond` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the next second, as determined by the current date and time on the system. |
| `DateTime.IsInPreviousHour` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the previous hour, as determined by the current date and time on the syst… |
| `DateTime.IsInPreviousMinute` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the previous minute, as determined by the current date and time on the sy… |
| `DateTime.IsInPreviousNHours` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the previous number of hours, as determined by the current date and time… |
| `DateTime.IsInPreviousNMinutes` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the previous number of minutes, as determined by the current date and tim… |
| `DateTime.IsInPreviousNSeconds` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the previous number of seconds, as determined by the current date and tim… |
| `DateTime.IsInPreviousSecond` | DateTime | nullable logical | ▶ | Indicates whether this datetime occurs during the previous second, as determined by the current date and time on the sy… |
| `DateTime.LocalNow` | DateTime | datetime |  | Returns the current date and time in the local timezone. |
| `DateTime.Time` | DateTime | nullable time | ▶ | Returns the time part of the given datetime value. |
| `DateTime.ToRecord` | DateTime | record | ▶ | Returns a record containing the datetime value's parts. |
| `DateTime.ToText` | DateTime | nullable text | ▶ | Returns a textual representation of the datetime value. |
| `DateTimeZone.FixedLocalNow` | DateTimeZone | datetimezone |  | Returns the current date & time in the local timezone. |
| `DateTimeZone.FixedUtcNow` | DateTimeZone | datetimezone |  | Returns the current date and time in UTC (the GMT timezone). |
| `DateTimeZone.From` | DateTimeZone | nullable datetimezone |  | Creates a datetimezone from the given value. |
| `DateTimeZone.FromFileTime` | DateTimeZone | nullable datetimezone |  | Creates a datetimezone from a 64 bits long number. |
| `DateTimeZone.FromText` | DateTimeZone | nullable datetimezone |  | Creates a datetimezone from local, universal, and custom datetimezone formats. |
| `DateTimeZone.LocalNow` | DateTimeZone | datetimezone |  | Returns the current date & time in the local timezone. |
| `DateTimeZone.RemoveZone` | DateTimeZone | nullable datetime |  | Removes timezone information from the given datetimezone value. |
| `DateTimeZone.SwitchZone` | DateTimeZone | nullable datetimezone |  | Changes the timezone of the value. |
| `DateTimeZone.ToLocal` | DateTimeZone | nullable datetimezone |  | Converts the timezone component to the local timezone. |
| `DateTimeZone.ToRecord` | DateTimeZone | record |  | Returns a record containing the datetimezone value's parts. |
| `DateTimeZone.ToText` | DateTimeZone | nullable text |  | Returns a textual representation of the datetimezone value. |
| `DateTimeZone.ToUtc` | DateTimeZone | nullable datetimezone |  | Converts the timezone component to UTC timezone. |
| `DateTimeZone.UtcNow` | DateTimeZone | datetimezone |  | Returns the current date and time in UTC (the GMT timezone). |
| `DateTimeZone.ZoneHours` | DateTimeZone | nullable number |  | Gets the timezone hour of the value. |
| `DateTimeZone.ZoneMinutes` | DateTimeZone | nullable number |  | Gets the timezone minutes of the value. |
| `DB2.Database` | Accessing data | table |  | Returns a table of SQL tables and views available in a Db2 database. |
| `Decimal.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a Decimal from the given value. |
| `DeltaLake.Metadata` | Accessing data | table |  | Given a Delta Lake table, returns the log entries for that table. |
| `DeltaLake.Table` | Accessing data | any |  | Returns the contents of the Delta Lake table. |
| `Diagnostics.ActivityId` | Diagnostics | nullable text |  | Returns an opaque identifier for the currently-running evaluation. |
| `Diagnostics.CorrelationId` | Diagnostics | nullable text |  | Returns an opaque identifier to correlate incoming requests with outgoing ones. |
| `Diagnostics.Trace` | Diagnostics | any |  | Writes a trace entry, if tracing is enabled, and returns the value. |
| `DirectQueryCapabilities.From` | Values.Implementation | table |  | This function is intended for internal use only. |
| `Double.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a Double from the given value. |
| `Duration.Days` | Duration | nullable number | ▶ | Returns the days portion of a duration. |
| `Duration.From` | Duration | nullable duration | ▶ | Creates a duration from the given value. |
| `Duration.FromText` | Duration | nullable duration | ▶ | Returns a duration value from textual elapsed time forms (d.h:m:s). |
| `Duration.Hours` | Duration | nullable number | ▶ | Returns the hours portion of a duration. |
| `Duration.Minutes` | Duration | nullable number | ▶ | Returns the minutes portion of a duration. |
| `Duration.Seconds` | Duration | nullable number | ▶ | Returns the seconds portion of a duration. |
| `Duration.ToRecord` | Duration | record | ▶ | Returns a record containing the parts of the duration. |
| `Duration.TotalDays` | Duration | nullable number | ▶ | Returns the total days this duration spans. |
| `Duration.TotalHours` | Duration | nullable number | ▶ | Returns the total hours this duration spans. |
| `Duration.TotalMinutes` | Duration | nullable number | ▶ | Returns the total minutes this duration spans. |
| `Duration.TotalSeconds` | Duration | nullable number | ▶ | Returns the total seconds this duration spans. |
| `Duration.ToText` | Duration | nullable text | ▶ | Returns the text of the form "d.h:m:s". |
| `Embedded.Value` | Values.Implementation | any |  | This function is intended for internal use only. |
| `Error.Record` | Error | record |  | Returns an error record from the provided text values for reason, message, detail, and error code. |
| `Essbase.Cubes` | Accessing data | table |  | Returns the cubes in an Essbase instance grouped by Essbase server. |
| `Excel.CurrentWorkbook` | Accessing data | table |  | Returns the contents of the current Excel workbook. |
| `Excel.ShapeTable` | Values.Implementation | any |  | This function is intended for internal use only. |
| `Excel.Workbook` | Accessing data | table |  | Returns the contents of the Excel workbook. |
| `Exchange.Contents` | Accessing data | table |  | Returns a table of contents from a Microsoft Exchange account. |
| `Expression.Constant` | Expression | text |  | Returns the M source code representation of a constant value. |
| `Expression.Evaluate` | Expression | any |  | Returns the result of evaluating an M expression. |
| `Expression.Identifier` | Expression | text |  | Returns the M source code representation of an identifier. |
| `File.Contents` | Accessing data | binary |  | Returns the contents of the specified file as binary. |
| `Folder.Contents` | Accessing data | table |  | Returns a table containing the properties and contents of the files and folders found in the specified folder. |
| `Folder.Files` | Accessing data | table |  | Returns a table containing the properties and contents of the files found in the specified folder and subfolders. |
| `Function.From` | Function | function |  | Creates a function with a specific parameter signature on top of a function that takes a single list argument. |
| `Function.Invoke` | Function | any |  | Invokes the given function. |
| `Function.InvokeAfter` | Function | any |  | Invokes the given function after the specified duration has passed. |
| `Function.InvokeWithErrorContext` | Values.Implementation | any |  | This function is intended for internal use only. |
| `Function.IsDataSource` | Type | logical | ▶ | Returns whether or not a particular function is considered a data source. |
| `Function.ScalarVector` | Function | function |  | Creates a scalar function on top of a vector function, batching multiple invocations. |
| `Geography.FromWellKnownText` | Record.Serialization | nullable record | ▶ | Translates text representing a geographic value in Well-Known Text (WKT) format into a structured record. |
| `Geography.ToWellKnownText` | Record.Serialization | nullable text | ▶ | Translates a structured geographic point value into its Well-Known Text (WKT) representation. |
| `GeographyPoint.From` | Record.Serialization | record | ▶ | Creates a record representing a geographic point from parts. |
| `Geometry.FromWellKnownText` | Record.Serialization | nullable record | ▶ | Translates text representing a geometric value in Well-Known Text (WKT) format into a structured record. |
| `Geometry.ToWellKnownText` | Record.Serialization | nullable text | ▶ | Translates a structured geometric point value into its Well-Known Text (WKT) representation. |
| `GeometryPoint.From` | Record.Serialization | record | ▶ | Creates a record representing a geometric point from parts. |
| `GoogleAnalytics.Accounts` | Accessing data | table |  | Returns Google Analytics accounts. |
| `Graph.Nodes` | Expression | list |  | This function is intended for internal use only. |
| `Guid.From` | Text.Conversions from and to text | nullable text |  | Returns a guid value from the given value. |
| `Hdfs.Contents` | Accessing data | table |  | Returns a table containing the properties and contents of the files and folders found in the specified folder from a Ha… |
| `Hdfs.Files` | Accessing data | table |  | Returns a table containing the properties and contents of the files found in the specified folder and subfolders from a… |
| `HdInsight.Containers` | Accessing data | table |  | Returns a navigational table containing the containers found in the specified account from an Azure storage vault. |
| `HdInsight.Contents` | Accessing data | table |  | Returns a navigational table containing the containers found in the specified account from an Azure storage vault. |
| `HdInsight.Files` | Accessing data | table |  | Returns a table containing the properties and contents of the blobs found in the specified container from an Azure stor… |
| `Html.Table` | Accessing data | table |  | Returns a table containing the results of running the specified CSS selectors against the provided HTML. |
| `Identity.From` | Accessing data | record |  | Creates an identity. |
| `Identity.IsMemberOf` | Accessing data | logical |  | Determines whether an identity is a member of an identity collection. |
| `IdentityProvider.Default` | Accessing data | any |  | The default identity provider for the current host. |
| `Informix.Database` | Accessing data | table |  | Returns a table of SQL tables and views available in an Informix database. |
| `Int16.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a 16-bit integer from the given value. |
| `Int32.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a 32-bit integer from the given value. |
| `Int64.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a 64-bit integer from the given value. |
| `Int8.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a signed 8-bit integer from the given value. |
| `ItemExpression.From` | Table.Table construction | record |  | Returns the abstract syntax tree (AST) for the body of a function. |
| `Json.Document` | Accessing data | any |  | Returns the content of the JSON document. |
| `Json.FromValue` | Text.Conversions from and to text | binary |  | Produces a JSON representation of a given value. |
| `Lines.FromBinary` | Lines | list |  | Converts a binary value to a list of text values split at lines breaks. |
| `Lines.FromText` | Lines | list |  | Converts a text value to a list of text values split at lines breaks. |
| `Lines.ToBinary` | Lines | binary |  | Converts a list of text into a binary value using the specified encoding and lineSeparator.The specified lineSeparator… |
| `Lines.ToText` | Lines | text |  | Converts a list of text into a single text. |
| `List.Accumulate` | List.Transformation functions | any | ▶ | Accumulates a summary value from the items in the list. |
| `List.AllTrue` | List.Membership functions | logical | ▶ | Returns true if all expressions are true. |
| `List.Alternate` | List.Selection | list | ▶ | Returns a list comprised of all the odd numbered offset elements in a list. |
| `List.AnyTrue` | List.Membership functions | logical | ▶ | Returns true if any expression is true. |
| `List.Average` | List.Averages | any | ▶ | Returns the average of the values. |
| `List.Buffer` | List.Selection | list | ▶ | Buffers a list. |
| `List.Combine` | List.Transformation functions | list | ▶ | Returns a single list by combining multiple lists. |
| `List.ConformToPageReader` | List.Transformation functions | table | ▶ | This function is intended for internal use only. |
| `List.Contains` | List.Membership functions | logical | ▶ | Indicates whether the list contains the value. |
| `List.ContainsAll` | List.Membership functions | logical | ▶ | Indicates where a list includes all the values in another list. |
| `List.ContainsAny` | List.Membership functions | logical | ▶ | Indicates where a list includes any of the values in another list. |
| `List.Count` | List.Information | number | ▶ | Returns the number of items in the list. |
| `List.Covariance` | List.Numerics | nullable number | ▶ | Returns the covariance between the two lists of numbers. |
| `List.Dates` | List.Generators | list | ▶ | Generates a list of date values given an initial value, count, and incremental duration value. |
| `List.DateTimes` | List.Generators | list | ▶ | Generates a list of datetime values given an initial value, count, and incremental duration value. |
| `List.DateTimeZones` | List.Generators | list | ▶ | Generates a list of datetimezone values given an initial value, count, and incremental duration value. |
| `List.Difference` | List.Set operations | list | ▶ | Returns the difference of the two given lists. |
| `List.Distinct` | List.Selection | list | ▶ | Returns a list of values with duplicates removed. |
| `List.Durations` | List.Generators | list | ▶ | Generates a list of duration values given an initial value, count, and incremental duration value. |
| `List.FindText` | List.Selection | list | ▶ | Returns a list of values (including record fields) that contain the specified text. |
| `List.First` | List.Selection | any | ▶ | Returns the first value of the list or the specified default if empty. |
| `List.FirstN` | List.Selection | any | ▶ | Returns the first set of items in the list by specifying how many items to return or a qualifying condition. |
| `List.Generate` | List.Generators | list | ▶ | Generates a list of values. |
| `List.InsertRange` | List.Selection | list | ▶ | Inserts values into a list at the given index. |
| `List.Intersect` | List.Set operations | list | ▶ | Returns the intersection of the list values found in the input. |
| `List.IsDistinct` | List.Selection | logical | ▶ | Indicates whether there are duplicates in the list. |
| `List.IsEmpty` | List.Information | logical | ▶ | Returns true if the list is empty. |
| `List.Last` | List.Selection | any | ▶ | Returns the last value of the list or the specified default if empty. |
| `List.LastN` | List.Selection | any | ▶ | Returns a list of the last item or items in the specified list. |
| `List.MatchesAll` | List.Selection | logical | ▶ | Returns true if the condition function is satisfied by all values in the list. |
| `List.MatchesAny` | List.Selection | logical | ▶ | Returns true if the condition function is satisfied by any value. |
| `List.Max` | List.Ordering | any | ▶ | Returns the maximum value or the default value for an empty list. |
| `List.MaxN` | List.Ordering | list | ▶ | Returns the maximum value(s) in the list. |
| `List.Median` | List.Ordering | any | ▶ | Returns the median value in the list. |
| `List.Min` | List.Ordering | any | ▶ | Returns the minimum value or the default value for an empty list. |
| `List.MinN` | List.Ordering | list | ▶ | Returns the minimum value(s) in the list. |
| `List.Mode` | List.Averages | any | ▶ | Returns the most frequent value in the list. |
| `List.Modes` | List.Averages | list | ▶ | Returns a list of the most frequent values in the list. |
| `List.NonNullCount` | List.Information | number | ▶ | Returns the number of non-null items in the list. |
| `List.Numbers` | List.Generators | list | ▶ | Returns a list of numbers given an initial value, count, and optional increment value. |
| `List.Percentile` | List.Ordering | any | ▶ | Returns one or more sample percentiles corresponding to the given probabilities. |
| `List.PositionOf` | List.Membership functions | any | ▶ | Returns the offset(s) of a value in a list. |
| `List.PositionOfAny` | List.Membership functions | any | ▶ | Returns the first offset of a value in a list. |
| `List.Positions` | List.Selection | list | ▶ | Returns a list of offsets for the input. |
| `List.Product` | List.Numerics | nullable number | ▶ | Returns the product of the numbers in the list. |
| `List.Random` | List.Generators | list | ▶ | Returns a list of random numbers. |
| `List.Range` | List.Selection | list | ▶ | Returns a subset of the list beginning at an offset. |
| `List.RemoveFirstN` | List.Transformation functions | list | ▶ | Returns a list that skips the specified number of elements at the beginning of the list. |
| `List.RemoveItems` | List.Transformation functions | list | ▶ | Removes items from list1 that are present in list. |
| `List.RemoveLastN` | List.Transformation functions | list | ▶ | Returns a list that removes the specified number of elements from the end of the list. |
| `List.RemoveMatchingItems` | List.Transformation functions | list | ▶ | Removes all occurrences of the input values. |
| `List.RemoveNulls` | List.Transformation functions | list | ▶ | Removes all "null" values from the specified list. |
| `List.RemoveRange` | List.Transformation functions | list | ▶ | Removes count number of values starting at the specified position. |
| `List.Repeat` | List.Transformation functions | list | ▶ | Returns a list that is count repetitions of the original list. |
| `List.ReplaceMatchingItems` | List.Transformation functions | list | ▶ | Applies each replacement of { old, new }. |
| `List.ReplaceRange` | List.Transformation functions | list | ▶ | Replaces count number of values starting at position with the replacement values. |
| `List.ReplaceValue` | List.Transformation functions | list | ▶ | Searches a list for the specified value and replaces it. |
| `List.Reverse` | List.Transformation functions | list | ▶ | Reverses the order of values in the list. |
| `List.Select` | List.Selection | list | ▶ | Returns a list of values that match the condition. |
| `List.Single` | List.Selection | any | ▶ | Returns the one list item for a list of length one, otherwise raises an error. |
| `List.SingleOrDefault` | List.Selection | any | ▶ | Returns the one list item for a list of length one and the default value for an empty list. |
| `List.Skip` | List.Selection | list | ▶ | Returns a list that skips the specified number of elements at the beginning of the list. |
| `List.Sort` | List.Ordering | list | ▶ | Sorts a list of data according to the criteria specified. |
| `List.Split` | List.Transformation functions | list | ▶ | Splits the specified list into a list of lists using the specified page size. |
| `List.StandardDeviation` | List.Averages | nullable number | ▶ | Returns a sample based estimate of the standard deviation. |
| `List.Sum` | List.Addition | any | ▶ | Returns the sum of the items in the list. |
| `List.Times` | List.Generators | list | ▶ | Generates a list of time values given an initial value, count, and incremental duration value. |
| `List.Transform` | List.Transformation functions | list | ▶ | Returns a new list of values computed from this list. |
| `List.TransformMany` | List.Transformation functions | list | ▶ | Returns a list whose elements are transformed from the input list using specified functions. |
| `List.Union` | List.Set operations | list | ▶ | Returns the union of the list values found in the input. |
| `List.Zip` | List.Transformation functions | list | ▶ | Returns a list of lists by combining items at the same position in multiple lists. |
| `Logical.From` | Logical | nullable logical | ▶ | Creates a logical from the given value. |
| `Logical.FromText` | Logical | nullable logical | ▶ | Creates a logical value from the text values "true" and "false". |
| `Logical.ToText` | Logical | nullable text | ▶ | Returns the text "true" or "false" given a logical value. |
| `Module.Versions` | Values.Implementation | record |  | Returns a record of module versions for the current module and its dependencies. |
| `MySQL.Database` | Accessing data | table |  | Returns a table of SQL tables, views, and stored scalar functions available in a MySQL database. |
| `Number.Abs` | Number.Operations | nullable number | ▶ | Returns the absolute value of the number. |
| `Number.Acos` | Number.Trigonometry | nullable number |  | Returns the arccosine of the number. |
| `Number.Asin` | Number.Trigonometry | nullable number |  | Returns the arcsine of the number. |
| `Number.Atan` | Number.Trigonometry | nullable number |  | Returns the arctangent of the number. |
| `Number.Atan2` | Number.Trigonometry | nullable number |  | Returns the arctangent of the division of the two numbers. |
| `Number.BitwiseAnd` | Number.Bytes | nullable number |  | Returns the result of performing a bitwise "And" operation between the two inputs. |
| `Number.BitwiseNot` | Number.Bytes | any |  | Returns a byte where each bit is the opposite of the input. |
| `Number.BitwiseOr` | Number.Bytes | nullable number |  | Returns the result of performing a bitwise "Or" between the two inputs. |
| `Number.BitwiseShiftLeft` | Number.Bytes | nullable number |  | Shifts the bits set to the left. |
| `Number.BitwiseShiftRight` | Number.Bytes | nullable number |  | Shifts the bits set to the right. |
| `Number.BitwiseXor` | Number.Bytes | nullable number |  | Returns the result of performing a bitwise "XOR" (Exclusive-OR) between the two inputs. |
| `Number.Combinations` | Number.Operations | nullable number | ▶ | Returns the number of unique combinations. |
| `Number.Cos` | Number.Trigonometry | nullable number |  | Returns the cosine of the number. |
| `Number.Cosh` | Number.Trigonometry | nullable number |  | Returns the hyperbolic cosine of the number. |
| `Number.Exp` | Number.Operations | nullable number | ▶ | Raises e to the given power. |
| `Number.Factorial` | Number.Operations | nullable number | ▶ | Returns the factorial of the number. |
| `Number.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a number from the given value. |
| `Number.FromText` | Number.Conversion and formatting | nullable number | ★▶ | Creates numbers from common text formats ("15", "3,423.10", "5.0E-10"). |
| `Number.IntegerDivide` | Number.Operations | nullable number | ▶ | Divides two numbers and returns the integer portion of the result. |
| `Number.IsEven` | Number.Information | logical |  | Indicates if the value is even. |
| `Number.IsNaN` | Number.Information | logical |  | Indicates if the value is NaN (Not a number). |
| `Number.IsOdd` | Number.Information | logical |  | Indicates if the value is odd. |
| `Number.Ln` | Number.Operations | nullable number | ▶ | Returns the natural logarithm of the number. |
| `Number.Log` | Number.Operations | nullable number | ▶ | Returns the logarithm of the number to the specified base (default e). |
| `Number.Log10` | Number.Operations | nullable number | ▶ | Returns the base 10 logarithm of the number. |
| `Number.Mod` | Number.Operations | nullable number | ▶ | Integer divides two numbers and returns the remainder. |
| `Number.Permutations` | Number.Operations | nullable number | ▶ | Returns the number of permutations. |
| `Number.Power` | Number.Operations | nullable number | ▶ | Raises a number to the given power. |
| `Number.Random` | Number.Random | number |  | Returns a random number. |
| `Number.RandomBetween` | Number.Random | number |  | Returns a random number between two numbers. |
| `Number.Round` | Number.Rounding | nullable number |  | Returns the rounded number. |
| `Number.RoundAwayFromZero` | Number.Rounding | nullable number |  | Returns the result of rounding positive numbers up and negative numbers down. |
| `Number.RoundDown` | Number.Rounding | nullable number |  | Returns the highest previous number. |
| `Number.RoundTowardZero` | Number.Rounding | nullable number |  | Returns the result of rounding positive numbers down and negative numbers up. |
| `Number.RoundUp` | Number.Rounding | nullable number |  | Returns the next highest number. |
| `Number.Sign` | Number.Operations | nullable number | ▶ | Returns 1 if the number is positive, -1 if it is negative, and 0 if it is zero. |
| `Number.Sin` | Number.Trigonometry | nullable number |  | Returns the sine of the number. |
| `Number.Sinh` | Number.Trigonometry | nullable number |  | Returns the hyperbolic sine of the number. |
| `Number.Sqrt` | Number.Operations | nullable number | ▶ | Returns the square root of the number. |
| `Number.Tan` | Number.Trigonometry | nullable number |  | Returns the tangent of the number. |
| `Number.Tanh` | Number.Trigonometry | nullable number |  | Returns the hyperbolic tangent of the number. |
| `Number.ToText` | Number.Conversion and formatting | nullable text | ▶ | Converts the given number to text. |
| `OData.Feed` | Accessing data | any |  | Returns a table of OData feeds offered by an OData service. |
| `Odbc.DataSource` | Accessing data | table |  | Returns a table of SQL tables and views from the ODBC data source. |
| `Odbc.InferOptions` | Accessing data | record |  | Returns the result of trying to infer SQL capabilities for an ODBC driver. |
| `Odbc.Query` | Accessing data | table |  | Returns the result of running a native query on an ODBC data source. |
| `OleDb.DataSource` | Accessing data | table |  | Returns a table of SQL tables and views from the OLE DB data source. |
| `OleDb.Query` | Accessing data | table |  | Returns the result of running a native query on an OLE DB data source. |
| `Oracle.Database` | Accessing data | table |  | Returns a table of SQL tables and views from the Oracle database. |
| `Parquet.Document` | Accessing data | any |  | Returns the contents of the Parquet document as a table. |
| `Parquet.Metadata` | Accessing data | any |  | This function is intended for internal use only. |
| `Pdf.Tables` | Accessing data | table |  | Returns any tables found in a PDF file. |
| `Percentage.From` | Number.Conversion and formatting | nullable number | ▶ | Returns a percentage value from the given value. |
| `PostgreSQL.Database` | Accessing data | table |  | Returns a table of SQL tables and views available in a PostgreSQL database. |
| `Progress.DataSourceProgress` | Values.Implementation | any |  | This function is intended for internal use only. |
| `RData.FromBinary` | Accessing data | any |  | Returns a record of data frames from the RData file. |
| `Record.AddField` | Record.Transformations | record | ▶ | Adds a field to a record. |
| `Record.Combine` | Record.Transformations | record | ▶ | Combines the records in the given list. |
| `Record.Field` | Record.Selection | any | ▶ | Returns the value of the specified field in a record. |
| `Record.FieldCount` | Record.Information | number | ▶ | Returns the number of fields in the record. |
| `Record.FieldNames` | Record.Selection | list | ▶ | Returns the names of the fields. |
| `Record.FieldOrDefault` | Record.Selection | any | ▶ | Returns the value of the specified field in a record or the default value if the field is not found. |
| `Record.FieldValues` | Record.Selection | list | ▶ | Returns a list of the field values. |
| `Record.FromList` | Record.Serialization | record | ▶ | Returns a record given a list of field values and a set of fields. |
| `Record.FromTable` | Record.Serialization | record | ▶ | Creates a record from a table of the form {[Name = name, Value = value]}. |
| `Record.HasFields` | Record.Information | logical | ▶ | Indicates whether the record has the specified fields. |
| `Record.RemoveFields` | Record.Transformations | record | ▶ | Removes the specified field(s) from the input record. |
| `Record.RenameFields` | Record.Transformations | record | ▶ | Applies rename(s) from a list in the form { old, new }. |
| `Record.ReorderFields` | Record.Transformations | record | ▶ | Reorders the record fields to match the order of a list of field names. |
| `Record.SelectFields` | Record.Selection | record | ▶ | Returns a record that contains only the specified fields. |
| `Record.ToList` | Record.Serialization | list | ▶ | Returns a list of values containing the field values of the input record. |
| `Record.ToTable` | Record.Serialization | table | ▶ | Returns a table with each row being a field name and value of the input record. |
| `Record.TransformFields` | Record.Transformations | record | ▶ | Returns a record after applying specified transformations. |
| `Replacer.ReplaceText` | Replacer | nullable text |  | Replaces text within the provided input. |
| `Replacer.ReplaceValue` | Replacer | any |  | Replaces values within the provided input. |
| `RowExpression.Column` | Table.Table construction | record |  | Returns an abstract syntax tree (AST) that represents access to a column within a row expression. |
| `RowExpression.From` | Table.Table construction | record |  | Returns the abstract syntax tree (AST) for the body of a function. |
| `Salesforce.Data` | Accessing data | table |  | Returns the objects from the Salesforce account. |
| `Salesforce.Reports` | Accessing data | table |  | Returns the reports from the Salesforce account. |
| `SapBusinessWarehouse.Cubes` | Accessing data | table |  | Returns the InfoCubes and queries in an SAP Business Warehouse system grouped by InfoArea. |
| `SapHana.Database` | Accessing data | table |  | Returns the packages in an SAP HANA database. |
| `SharePoint.Contents` | Accessing data | table |  | Returns a table containing content from a SharePoint site. |
| `SharePoint.Files` | Accessing data | table |  | Returns a table containing documents from a SharePoint site. |
| `SharePoint.Tables` | Accessing data | table |  | Returns a table containing content from a SharePoint List. |
| `Single.From` | Number.Conversion and formatting | nullable number | ▶ | Creates a Single from the given value. |
| `Soda.Feed` | Accessing data | table |  | Returns a table from the contents at the specified URL formatted according to the SODA 2.0 API. |
| `Splitter.SplitByNothing` | Splitter | function | ▶ | Returns a function that does no splitting, returning its argument as a single element list. |
| `Splitter.SplitTextByAnyDelimiter` | Splitter | function | ▶ | Returns a function that splits text into a list of text at any of the specified delimiters. |
| `Splitter.SplitTextByCharacterTransition` | Splitter | function | ▶ | Returns a function that splits text into a list of text according to a transition from one kind of character to another. |
| `Splitter.SplitTextByDelimiter` | Splitter | function | ▶ | Returns a function that splits text into a list of text according to the specified delimiter. |
| `Splitter.SplitTextByEachDelimiter` | Splitter | function | ▶ | Returns a function that splits text into a list of text at each specified delimiter in sequence. |
| `Splitter.SplitTextByLengths` | Splitter | function | ▶ | Returns a function that splits text into a list of text by each specified length. |
| `Splitter.SplitTextByPositions` | Splitter | function | ▶ | Returns a function that splits text into a list of text at each specified position. |
| `Splitter.SplitTextByRanges` | Splitter | function | ▶ | Returns a function that splits text into a list of text according to the specified offsets and lengths. |
| `Splitter.SplitTextByRepeatedLengths` | Splitter | function | ▶ | Returns a function that splits text into a list of text after the specified length repeatedly. |
| `Splitter.SplitTextByWhitespace` | Splitter | function | ▶ | Returns a function that splits text into a list of text at whitespace. |
| `Sql.Database` | Accessing data | table |  | Returns a table of SQL tables, views, and stored functions from the SQL Server database. |
| `Sql.Databases` | Accessing data | table |  | Returns a table of databases on a SQL Server. |
| `SqlExpression.SchemaFrom` | Values.Implementation | any |  | This function is intended for internal use only. |
| `SqlExpression.ToExpression` | Values.Implementation | text |  | Converts the provided SQL query to M code. |
| `Sybase.Database` | Accessing data | table |  | Returns a table of SQL tables and views available in a Sybase database. |
| `Table.AddColumn` | Table.Transformation | table | ★▶ | Adds a column with the specified name. |
| `Table.AddFuzzyClusterColumn` | Table.Transformation | table | ▶ | Adds a new column with representative values obtained by fuzzy grouping values of the specified column in the table. |
| `Table.AddIndexColumn` | Table.Transformation | table | ▶ | Appends a column with explicit position values. |
| `Table.AddJoinColumn` | Table.Transformation | table | ▶ | Performs a join between tables on supplied columns and produces the join result in a new column. |
| `Table.AddKey` | Table.Transformation | table | ▶ | Adds a key to a table. |
| `Table.AddRankColumn` | Table.Ordering | table | ▶ | Appends a column with the ranking of one or more other columns. |
| `Table.AggregateTableColumn` | Table.Transformation | table | ▶ | Aggregates a column of tables into multiple columns in the containing table. |
| `Table.AlternateRows` | Table.Row operations | table | ▶ | Keeps the initial offset then alternates taking and skipping the following rows. |
| `Table.ApproximateRowCount` | Table.Information | number | ▶ | Returns the approximate number of rows in the table. |
| `Table.Buffer` | Table.Other | table | ▶ | Buffers a table in memory, isolating it from external changes during evaluation. |
| `Table.ClearDown` | Table.Transformation | table | ▶ | Clears repeating sets of column values. |
| `Table.Column` | Table.Column operations | list | ▶ | Returns a specified column of data from the table as a list. |
| `Table.ColumnCount` | Table.Information | number | ▶ | Returns the number of columns in the table. |
| `Table.ColumnNames` | Table.Column operations | list | ▶ | Returns the column names as a list. |
| `Table.ColumnsOfType` | Table.Column operations | list | ▶ | Returns a list with the names of the columns that match the specified types. |
| `Table.Combine` | Table.Row operations | table | ▶ | Returns a table that is the result of merging a list of tables. |
| `Table.CombineColumns` | Table.Transformation | table | ▶ | Combines the specified columns into a new column using the specified combiner function. |
| `Table.CombineColumnsToRecord` | Table.Transformation | table | ▶ | Combines the specified columns into a new record-valued column where each record has field names and values correspondi… |
| `Table.ConformToPageReader` | Table.Transformation | table | ▶ | This function is intended for internal use only. |
| `Table.Contains` | Table.Membership | logical | ▶ | Indicates whether the specified record appears as a row in the table. |
| `Table.ContainsAll` | Table.Membership | logical | ▶ | Indicates whether all of the specified records appear as rows in the table. |
| `Table.ContainsAny` | Table.Membership | logical | ▶ | Indicates whether any of the specified records appear as rows in the table. |
| `Table.DemoteHeaders` | Table.Column operations | table | ▶ | Demotes the column headers to the first row of values. |
| `Table.Distinct` | Table.Membership | table | ★▶ | Removes duplicate rows from the table. |
| `Table.DuplicateColumn` | Table.Column operations | table | ▶ | Duplicates a column with the specified name. |
| `Table.ExpandListColumn` | Table.Transformation | table | ▶ | Given a column of lists in a table, create a copy of a row for each value in its list. |
| `Table.ExpandRecordColumn` | Table.Transformation | table | ▶ | Expands a column of records into columns with each of the values. |
| `Table.ExpandTableColumn` | Table.Transformation | table | ▶ | Expands a column of records or a column of tables into multiple columns in the containing table. |
| `Table.FillDown` | Table.Transformation | table | ▶ | Propagates the value of a previous cell to the null-valued cells below in the column. |
| `Table.FillUp` | Table.Transformation | table | ▶ | Propagates the value of a cell to the null-valued cells above in the column. |
| `Table.FilterWithDataTable` | Table.Transformation | any |  | This function is intended for internal use only. |
| `Table.FindText` | Table.Row operations | table | ▶ | Returns all the rows that contain the given text in the table. |
| `Table.First` | Table.Row operations | any | ▶ | Returns the first row or a specified default value. |
| `Table.FirstN` | Table.Row operations | table | ▶ | Returns the first count rows specified. |
| `Table.FirstValue` | Table.Row operations | any | ▶ | Returns the first column of the first row of the table or a specified default value. |
| `Table.FromColumns` | Table.Table construction | table | ▶ | Creates a table from a list of columns and specified values. |
| `Table.FromList` | Table.Table construction | table | ▶ | Converts a list into a table by applying the specified splitting function to each item in the list. |
| `Table.FromPartitions` | Table.Row operations | table | ▶ | Returns a table that is the result of combining a set of partitioned tables. |
| `Table.FromRecords` | Table.Table construction | table | ▶ | Converts a list of records into a table. |
| `Table.FromRows` | Table.Table construction | table | ▶ | Creates a table from a list of row values and optional columns. |
| `Table.FromValue` | Table.Table construction | table | ▶ | Creates a table with a column from the provided value(s). |
| `Table.FuzzyGroup` | Table.Transformation | table | ▶ | Groups rows in the table based on fuzzy matching of keys. |
| `Table.FuzzyJoin` | Table.Transformation | table | ▶ | Joins the rows from the two tables that fuzzy match based on the given keys. |
| `Table.FuzzyNestedJoin` | Table.Transformation | table | ▶ | Performs a fuzzy join between tables on supplied columns and produces the join result in a new column. |
| `Table.Group` | Table.Transformation | table | ▶ | Groups rows in the table that have the same key. |
| `Table.HasColumns` | Table.Column operations | logical | ▶ | Indicates whether the table contains the specified column(s). |
| `Table.InsertRows` | Table.Row operations | table | ▶ | Inserts a list of rows into the table at the specified position. |
| `Table.IsDistinct` | Table.Membership | logical | ▶ | Indicates whether the table contains only distinct rows (no duplicates). |
| `Table.IsEmpty` | Table.Information | logical | ▶ | Indicates whether the table contains any rows. |
| `Table.Join` | Table.Transformation | table | ★▶ | Joins the rows from the two tables that match based on the given keys. |
| `Table.Keys` | Table.Transformation | list | ▶ | Returns the keys of the specified table. |
| `Table.Last` | Table.Row operations | any | ▶ | Returns the last row or a specified default value. |
| `Table.LastN` | Table.Row operations | table | ▶ | Returns the last specified number of rows. |
| `Table.MatchesAllRows` | Table.Row operations | logical | ▶ | Indicates whether all the rows in the table meet the given condition. |
| `Table.MatchesAnyRows` | Table.Row operations | logical | ▶ | Indicates whether any the rows in the table meet the given condition. |
| `Table.Max` | Table.Ordering | any | ▶ | Returns the largest row or default value using the given criteria. |
| `Table.MaxN` | Table.Ordering | table | ▶ | Returns the largest row(s) using the given criteria. |
| `Table.Min` | Table.Ordering | any | ▶ | Returns the smallest row or a default value using the given criteria. |
| `Table.MinN` | Table.Ordering | table | ▶ | Returns the smallest row(s) using the given criteria. |
| `Table.NestedJoin` | Table.Transformation | table | ▶ | Performs a join between tables on supplied columns and produces the join result in a new column. |
| `Table.Partition` | Table.Row operations | list | ▶ | Partitions the table into a list of tables based on the number of groups and column specified. |
| `Table.PartitionKey` | Table.Transformation | nullable list | ▶ | Returns the partition key of the specified table. |
| `Table.PartitionValues` | Table.Information | table | ▶ | Returns information about how a table is partitioned. |
| `Table.Pivot` | Table.Column operations | table | ▶ | Given a pair of columns representing attribute-value pairs, rotates the data in the attribute column into a column head… |
| `Table.PositionOf` | Table.Membership | any | ▶ | Returns the position or positions of the row within the table. |
| `Table.PositionOfAny` | Table.Membership | any | ▶ | Returns the position or positions of any of the specified rows within the table. |
| `Table.PrefixColumns` | Table.Column operations | table | ▶ | Returns a table where the columns have all been prefixed with the given text. |
| `Table.Profile` | Table.Information | table | ▶ | Returns a profile of the columns of a table. |
| `Table.PromoteHeaders` | Table.Column operations | table | ▶ | Promotes the first row of values as the new column headers (i.e. |
| `Table.Range` | Table.Row operations | table | ▶ | Returns the rows beginning at the specified offset. |
| `Table.RemoveColumns` | Table.Column operations | table | ▶ | Removes the specified columns. |
| `Table.RemoveFirstN` | Table.Row operations | table | ▶ | Returns a table with the first count rows skipped. |
| `Table.RemoveLastN` | Table.Row operations | table | ▶ | Returns a table with the last N rows removed. |
| `Table.RemoveMatchingRows` | Table.Membership | table | ▶ | Removes all occurrences of the specified rows from the table. |
| `Table.RemoveRows` | Table.Row operations | table | ▶ | Removes the specified number of rows. |
| `Table.RemoveRowsWithErrors` | Table.Row operations | table | ▶ | Returns a table with the rows removed from the input table that contain an error in at least one of the cells. |
| `Table.RenameColumns` | Table.Column operations | table | ▶ | Applies rename(s) of the form {old, new}. |
| `Table.ReorderColumns` | Table.Column operations | table | ▶ | Returns a table with the columns in the specified order. |
| `Table.Repeat` | Table.Row operations | table | ▶ | Repeats the rows of the tables a specified number of times. |
| `Table.ReplaceErrorValues` | Table.Transformation | table | ▶ | Replaces the error values in the specified columns with the corresponding specified value. |
| `Table.ReplaceKeys` | Table.Transformation | table | ▶ | Replaces the keys of the specified table. |
| `Table.ReplaceMatchingRows` | Table.Membership | table | ▶ | Replaces all the specified rows with the provided row(s). |
| `Table.ReplacePartitionKey` | Table.Transformation | table | ▶ | Replaces the partition key of the specified table. |
| `Table.ReplaceRelationshipIdentity` | Table.Transformation | any | ▶ | This function is intended for internal use only. |
| `Table.ReplaceRows` | Table.Row operations | table | ▶ | Replaces the specified range of rows with the provided row(s). |
| `Table.ReplaceValue` | Table.Transformation | table | ▶ | Replaces one value with another in the specified columns. |
| `Table.ReverseRows` | Table.Row operations | table | ▶ | Returns a table with the rows in reverse order. |
| `Table.RowCount` | Table.Information | number | ▶ | Returns the number of rows in the table. |
| `Table.Schema` | Table.Information | table | ▶ | Returns a table containing a description of the columns (i.e. |
| `Table.SelectColumns` | Table.Column operations | table | ▶ | Returns a table with only the specified columns. |
| `Table.SelectRows` | Table.Row operations | table | ▶ | Selects the rows that meet the condition function. |
| `Table.SelectRowsWithErrors` | Table.Row operations | table | ▶ | Returns a table with only those rows of the input table that contain an error in at least one of the cells. |
| `Table.SingleRow` | Table.Row operations | record | ▶ | Returns the single row in the table. |
| `Table.Skip` | Table.Row operations | table | ▶ | Returns a table with the first count rows skipped. |
| `Table.Sort` | Table.Ordering | table | ▶ | Sorts the table using one or more column names and comparison criteria. |
| `Table.Split` | Table.Transformation | list | ▶ | Splits the specified table into a list of tables using the specified page size. |
| `Table.SplitAt` | Table.Row operations | list | ▶ | Returns a list containing the first count rows specified and the remaining rows. |
| `Table.SplitColumn` | Table.Transformation | table | ▶ | Splits the specified column into a set of additional columns using the specified splitter function. |
| `Table.StopFolding` | Table.Other | table | ▶ | Prevents any downstream operations from being run against the original source of the data. |
| `Table.ToColumns` | Table.Conversions | list | ▶ | Creates a list of nested lists of column values from a table. |
| `Table.ToList` | Table.Conversions | list | ▶ | Converts a table into a list by applying the specified combining function to each row of values in the table. |
| `Table.ToRecords` | Table.Conversions | list | ▶ | Converts a table to a list of records. |
| `Table.ToRows` | Table.Conversions | list | ▶ | Creates a list of nested lists of row values from a table. |
| `Table.TransformColumnNames` | Table.Column operations | table | ▶ | Transforms column names by using the given function. |
| `Table.TransformColumns` | Table.Transformation | table | ▶ | Transforms the values of one or more columns. |
| `Table.TransformColumnTypes` | Table.Transformation | table | ★▶ | Applies type transformation(s) of the form { column, type } using a specific culture. |
| `Table.TransformRows` | Table.Transformation | list | ▶ | Transforms the rows of the table using the specified transform function. |
| `Table.Transpose` | Table.Transformation | table | ▶ | Makes columns into rows and rows into columns. |
| `Table.Unpivot` | Table.Column operations | table | ▶ | Translates a set of columns in a table into attribute-value pairs. |
| `Table.UnpivotOtherColumns` | Table.Column operations | table | ▶ | Translates all columns other than a specified set into attribute-value pairs. |
| `Table.View` | Table.Table construction | table | ▶ | Creates or extends a table with user-defined handlers for query and action operations. |
| `Table.ViewError` | Table.Table construction | record | ▶ | Creates a modified error record which won't trigger a fallback when raised by a handler defined on a view (via Table.Vi… |
| `Table.ViewFunction` | Table.Table construction | function | ▶ | Creates a function that can be intercepted by a handler defined on a view (via Table.View). |
| `Table.WithErrorContext` | Values.Implementation | any | ▶ | This function is intended for internal use only. |
| `Tables.GetRelationships` | Table.Information | table |  | Gets the relationships among a set of tables. |
| `Teradata.Database` | Accessing data | table |  | Returns a table of SQL tables and views from the Teradata database. |
| `Text.AfterDelimiter` | Text.Transformations | any | ▶ | Text.AfterDelimiter |
| `Text.At` | Text.Extraction | nullable text | ▶ | Returns the character at the specified position. |
| `Text.BeforeDelimiter` | Text.Transformations | any | ▶ | Text.BeforeDelimiter |
| `Text.BetweenDelimiters` | Text.Transformations | any | ▶ | Text.BetweenDelimiters |
| `Text.Clean` | Text.Transformations | nullable text | ▶ | Returns the text value with all control characters removed. |
| `Text.Combine` | Text.Transformations | text | ▶ | Concatenates a list of text values into one text value. |
| `Text.Contains` | Text.Membership | nullable logical | ▶ | Returns whether the text contains the substring. |
| `Text.End` | Text.Extraction | nullable text | ▶ | Returns the last characters of the text. |
| `Text.EndsWith` | Text.Membership | nullable logical | ▶ | Indicates whether the text ends in the specified value. |
| `Text.Format` | Text.Conversions from and to text | text | ▶ | Returns formatted text from a format string and arguments. |
| `Text.From` | Text.Conversions from and to text | nullable text | ▶ | Creates a text value from the given value. |
| `Text.FromBinary` | Text.Conversions from and to text | nullable text | ▶ | Decodes data from a binary form into text. |
| `Text.InferNumberType` | Text | type | ▶ | Infers the granular number type (Int64.Type, Double.Type, and so on) of a number encoded in text. |
| `Text.Insert` | Text.Modification | nullable text | ▶ | Inserts one text value into another at a given position. |
| `Text.Length` | Text.Information | nullable number | ▶ | Returns the number of characters. |
| `Text.Lower` | Text.Transformations | nullable text | ▶ | Converts all characters to lowercase. |
| `Text.Middle` | Text.Extraction | nullable text | ▶ | Returns the substring up to a specific length. |
| `Text.NewGuid` | Text.Conversions from and to text | text | ▶ | Returns a new, random globally unique identifier (GUID). |
| `Text.PadEnd` | Text.Transformations | nullable text | ▶ | Returns text of a specified length by padding the end of the given text. |
| `Text.PadStart` | Text.Transformations | nullable text | ▶ | Returns text of a specified length by padding the start of the given text. |
| `Text.PositionOf` | Text.Membership | any | ▶ | Returns the first position of the value (-1 if not found). |
| `Text.PositionOfAny` | Text.Membership | any | ▶ | Returns the first position in the text value of any listed character (-1 if not found). |
| `Text.Proper` | Text.Transformations | nullable text | ▶ | Capitalizes the first letter of each word. |
| `Text.Range` | Text.Extraction | nullable text | ▶ | Returns the substring found at offset. |
| `Text.Remove` | Text.Modification | nullable text | ▶ | Removes all occurrences of the given character or list of characters from the input text value. |
| `Text.RemoveRange` | Text.Modification | nullable text | ▶ | Removes a count of characters starting at the given offset |
| `Text.Repeat` | Text.Transformations | nullable text | ▶ | Returns a text value composed of the input text repeated a specified number of times. |
| `Text.Replace` | Text.Modification | nullable text | ▶ | Replaces all occurrences of the given substring in the text. |
| `Text.ReplaceRange` | Text.Modification | nullable text | ▶ | Removes a range of characters and inserts a new value at a specified position. |
| `Text.Reverse` | Text.Transformations | nullable text | ▶ | Text.Reverse |
| `Text.Select` | Text.Modification | nullable text | ▶ | Selects all occurrences of the given character or list of characters from the input text value. |
| `Text.Split` | Text.Transformations | list | ▶ | Splits text into a list of text values based upon a specified delimiter. |
| `Text.SplitAny` | Text.Transformations | list | ▶ | Returns a list of text values, split on any of the characters in the delimiter. |
| `Text.Start` | Text.Extraction | nullable text | ▶ | Returns the start of the text. |
| `Text.StartsWith` | Text.Membership | nullable logical | ▶ | Indicates whether the text starts with a specified value. |
| `Text.ToBinary` | Text.Conversions from and to text | nullable binary | ▶ | Encodes text into a binary form. |
| `Text.ToList` | Text.Conversions from and to text | list | ▶ | Returns a list of character values from the given text value. |
| `Text.Trim` | Text.Transformations | nullable text | ▶ | Removes all the specified leading and trailing characters. |
| `Text.TrimEnd` | Text.Transformations | nullable text | ▶ | Removes all specified trailing characters. |
| `Text.TrimStart` | Text.Transformations | nullable text | ▶ | Removes all specified leading characters. |
| `Text.Upper` | Text.Transformations | nullable text | ▶ | Converts all characters to uppercase. |
| `Time.EndOfHour` | Date | any | ▶ | Returns the end of the hour. |
| `Time.From` | Time | nullable time |  | Creates a time from the given value. |
| `Time.FromText` | Time | nullable time |  | Creates a Time from local and universal, and custom Time formats. |
| `Time.Hour` | Time | nullable number |  | Returns the hour component. |
| `Time.Minute` | Time | nullable number |  | Returns the minute component. |
| `Time.Second` | Time | nullable number |  | Returns the second component. |
| `Time.StartOfHour` | Date | any | ▶ | Returns the start of the hour. |
| `Time.ToRecord` | Time | record |  | Returns a record containing the Time value's parts. |
| `Time.ToText` | Time | nullable text |  | Returns a textual representation of the time value. |
| `Type.AddTableKey` | Type | type | ▶ | Adds a key to the given table type. |
| `Type.ClosedRecord` | Type | type | ▶ | Returns a closed version of the given record type (or the same type, if it is already closed). |
| `Type.Facets` | Type | record | ▶ | Returns the facets of a type. |
| `Type.ForFunction` | Type | type | ▶ | Returns a type that represents functions with specific parameter and return type constraints. |
| `Type.ForRecord` | Type | type | ▶ | Returns a type that represents records with specific type constraints on fields. |
| `Type.FunctionParameters` | Type | record | ▶ | Returns a record with field values set to the name of the parameters of a function type, and their values set to their… |
| `Type.FunctionRequiredParameters` | Type | number | ▶ | Returns a number indicating the minimum number of parameters required to invoke the type of function. |
| `Type.FunctionReturn` | Type | type | ▶ | Returns a type returned by a function type. |
| `Type.Is` | Type | logical | ▶ | Determines if a value of the first type is always compatible with the second type. |
| `Type.IsNullable` | Type | logical | ▶ | Returns true if a type is a nullable type; otherwise, false. |
| `Type.IsOpenRecord` | Type | logical | ▶ | Returns whether a record type is open. |
| `Type.ListItem` | Type | type | ▶ | Returns an item type from a list type. |
| `Type.NonNullable` | Type | type | ▶ | Returns the non nullable type from a type. |
| `Type.OpenRecord` | Type | type | ▶ | Returns an opened version of the given record type (or the same type, if it is already open). |
| `Type.RecordFields` | Type | record | ▶ | Returns a record describing the fields of a record type with each field of the returned record type having a correspond… |
| `Type.ReplaceFacets` | Type | type | ▶ | Replaces the facets of a type. |
| `Type.ReplaceTableKeys` | Type | type | ▶ | Returns a new table type with all keys replaced by the specified list of keys. |
| `Type.ReplaceTablePartitionKey` | Type | type | ▶ | Returns a new table type with the partition key replaced by the specified partition key. |
| `Type.TableColumn` | Type | type | ▶ | Returns the type of a column in a table. |
| `Type.TableKeys` | Type | list | ▶ | Returns the possibly empty list of keys for the given table type. |
| `Type.TablePartitionKey` | Type | nullable list | ▶ | Returns the partition key for the given table type if it has one. |
| `Type.TableRow` | Type | type | ▶ | Returns the row type of the table type. |
| `Type.TableSchema` | Type | table | ▶ | Returns a table containing a description of the columns (i.e. |
| `Type.Union` | Type | type | ▶ | Returns the union of a list of types. |
| `Uri.BuildQueryString` | Uri | text |  | Assemble a record into a URI query string. |
| `Uri.Combine` | Uri | text |  | Returns an absolute URI that is the combination of the input base URI and relative URI. |
| `Uri.EscapeDataString` | Uri | text |  | Encodes special characters in accordance with RFC 3986. |
| `Uri.Parts` | Uri | record |  | Returns the parts of the input absolute URI as a record. |
| `Value.Add` | Values.Arithmetic operations | any |  | Returns the sum of the two values. |
| `Value.Alternates` | Expression | any |  | Expresses alternate query plans. |
| `Value.As` | Values.Types | any |  | Returns the value if it's compatible with the specified type. |
| `Value.Compare` | Values | number |  | Returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second. |
| `Value.Divide` | Values.Arithmetic operations | any |  | Returns the result of dividing the first value by the second. |
| `Value.Equals` | Values | logical |  | Returns whether two values are equal. |
| `Value.Expression` | Expression | nullable record |  | Returns an abstract syntax tree (AST) that represents the value's expression. |
| `Value.Firewall` | Values.Implementation | any |  | This function is intended for internal use only. |
| `Value.FromText` | Text.Conversions from and to text | any |  | Creates a strongly-typed value from a textual representation. |
| `Value.Is` | Values.Types | logical |  | Determines whether a value is compatible with the specified type. |
| `Value.Lineage` | Expression | any |  | This function is intended for internal use only. |
| `Value.Metadata` | Metadata | any |  | Returns a record containing the input's metadata. |
| `Value.Multiply` | Values.Arithmetic operations | any |  | Returns the product of the two values. |
| `Value.NativeQuery` | Values | any |  | Evaluates a query against a target. |
| `Value.NullableEquals` | Values | nullable logical |  | Returns whether two values are equal. |
| `Value.Optimize` | Expression | any |  | Signals Value.Expression to return the optimized expression for a value. |
| `Value.RemoveMetadata` | Metadata | any |  | Strips the input of metadata. |
| `Value.ReplaceMetadata` | Metadata | any |  | Replaces the input's metadata information. |
| `Value.ReplaceType` | Values.Types | any |  | Replaces the value's type. |
| `Value.ResourceExpression` | Value | any |  | Value.ResourceExpression |
| `Value.Subtract` | Values.Arithmetic operations | any |  | Returns the difference of the two values. |
| `Value.Traits` | Expression | table |  | This function is intended for internal use only. |
| `Value.Type` | Values | type |  | Returns the type of the given value. |
| `Value.VersionIdentity` | Action | any |  | Returns the version identity of the value. |
| `Value.Versions` | Action | table |  | Returns a navigation table containing the available versions of the value. |
| `Value.ViewError` | Values.Implementation | record |  | This function is intended for internal use only. |
| `Value.ViewFunction` | Values.Implementation | function |  | This function is intended for internal use only. |
| `Variable.Value` | Values.Implementation | any |  | Returns the value of the specified variable. |
| `Variable.ValueOrDefault` | Values.Implementation | any |  | Returns the value of the specified variable or the default value if the variable is not defined. |
| `Web.BrowserContents` | Accessing data | text |  | Returns the HTML for the specified URL, as viewed by a web browser. |
| `Web.Contents` | Accessing data | binary |  | Returns the contents downloaded from the url as binary. |
| `Web.Headers` | Accessing data | record |  | Returns the HTTP headers downloaded from the url as a record value. |
| `Web.Page` | Accessing data | table |  | Returns the contents of the HTML document broken into its constituent structures, as well as a representation of the fu… |
| `WebAction.Request` | Action | any |  | Creates an action that, when executed, will return the results of performing an HTTP request as a binary value. |
| `Xml.Document` | Accessing data | table |  | Returns the contents of the XML document as a hierarchical table. |
| `Xml.Tables` | Accessing data | table |  | Returns the contents of the XML document as a nested collection of flattened tables. |
