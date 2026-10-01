# Review PBIPs

One Power BI project per example category, to read the executed examples in Power BI instead
of in Markdown. The example pages stay the source of truth; these projects are generated from
them.

The table on the first page shows, for each block, the function's description as the engine
documents it (from its card under `generated/library/`), the code, the result recorded on the
page and the result this Power BI returns after Refresh.

| Batch | Project |
|---|---|
| Binary Formats.Controlling byte order | [binary-formats-controlling-byte-order/BinaryFormatsControllingByteOrder.pbip](binary-formats-controlling-byte-order/BinaryFormatsControllingByteOrder.pbip) |
| Binary Formats.Controlling what comes next | [binary-formats-controlling-what-comes-next/BinaryFormatsControllingWhatComesNext.pbip](binary-formats-controlling-what-comes-next/BinaryFormatsControllingWhatComesNext.pbip) |
| Binary Formats.Limiting input | [binary-formats-limiting-input/BinaryFormatsLimitingInput.pbip](binary-formats-limiting-input/BinaryFormatsLimitingInput.pbip) |
| Binary Formats.Reading a group of items | [binary-formats-reading-a-group-of-items/BinaryFormatsReadingAGroupOfItems.pbip](binary-formats-reading-a-group-of-items/BinaryFormatsReadingAGroupOfItems.pbip) |
| Binary Formats.Reading binary data | [binary-formats-reading-binary-data/BinaryFormatsReadingBinaryData.pbip](binary-formats-reading-binary-data/BinaryFormatsReadingBinaryData.pbip) |
| Binary Formats.Reading lists | [binary-formats-reading-lists/BinaryFormatsReadingLists.pbip](binary-formats-reading-lists/BinaryFormatsReadingLists.pbip) |
| Binary Formats.Reading numbers | [binary-formats-reading-numbers/BinaryFormatsReadingNumbers.pbip](binary-formats-reading-numbers/BinaryFormatsReadingNumbers.pbip) |
| Binary Formats.Reading records | [binary-formats-reading-records/BinaryFormatsReadingRecords.pbip](binary-formats-reading-records/BinaryFormatsReadingRecords.pbip) |
| Binary Formats.Reading text | [binary-formats-reading-text/BinaryFormatsReadingText.pbip](binary-formats-reading-text/BinaryFormatsReadingText.pbip) |
| Binary Formats.Transforming what was read | [binary-formats-transforming-what-was-read/BinaryFormatsTransformingWhatWasRead.pbip](binary-formats-transforming-what-was-read/BinaryFormatsTransformingWhatWasRead.pbip) |
| Binary | [binary/Binary.pbip](binary/Binary.pbip) |
| Date | [date/Date.pbip](date/Date.pbip) |
| DateTime | [datetime/DateTime.pbip](datetime/DateTime.pbip) |
| Duration | [duration/Duration.pbip](duration/Duration.pbip) |
| List.Addition | [list-addition/ListAddition.pbip](list-addition/ListAddition.pbip) |
| List.Averages | [list-averages/ListAverages.pbip](list-averages/ListAverages.pbip) |
| List.Generators | [list-generators/ListGenerators.pbip](list-generators/ListGenerators.pbip) |
| List.Information | [list-information/ListInformation.pbip](list-information/ListInformation.pbip) |
| List.Membership functions | [list-membership-functions/ListMembershipFunctions.pbip](list-membership-functions/ListMembershipFunctions.pbip) |
| List.Numerics | [list-numerics/ListNumerics.pbip](list-numerics/ListNumerics.pbip) |
| List.Ordering | [list-ordering/ListOrdering.pbip](list-ordering/ListOrdering.pbip) |
| List.Selection | [list-selection/ListSelection.pbip](list-selection/ListSelection.pbip) |
| List.Set operations | [list-set-operations/ListSetOperations.pbip](list-set-operations/ListSetOperations.pbip) |
| List.Transformation functions | [list-transformation-functions/ListTransformationFunctions.pbip](list-transformation-functions/ListTransformationFunctions.pbip) |
| Logical | [logical/Logical.pbip](logical/Logical.pbip) |
| Number.Conversion and formatting | [number-conversion-and-formatting/NumberConversionAndFormatting.pbip](number-conversion-and-formatting/NumberConversionAndFormatting.pbip) |
| Number.Operations | [number-operations/NumberOperations.pbip](number-operations/NumberOperations.pbip) |
| Record.Information | [record-information/RecordInformation.pbip](record-information/RecordInformation.pbip) |
| Record.Selection | [record-selection/RecordSelection.pbip](record-selection/RecordSelection.pbip) |
| Record.Serialization | [record-serialization/RecordSerialization.pbip](record-serialization/RecordSerialization.pbip) |
| Record.Transformations | [record-transformations/RecordTransformations.pbip](record-transformations/RecordTransformations.pbip) |
| Splitter | [splitter/Splitter.pbip](splitter/Splitter.pbip) |
| Table.Column operations | [table-column-operations/TableColumnOperations.pbip](table-column-operations/TableColumnOperations.pbip) |
| Table.Conversions | [table-conversions/TableConversions.pbip](table-conversions/TableConversions.pbip) |
| Table.Information | [table-information/TableInformation.pbip](table-information/TableInformation.pbip) |
| Table.Membership | [table-membership/TableMembership.pbip](table-membership/TableMembership.pbip) |
| Table.Ordering | [table-ordering/TableOrdering.pbip](table-ordering/TableOrdering.pbip) |
| Table.Other | [table-other/TableOther.pbip](table-other/TableOther.pbip) |
| Table.Row operations | [table-row-operations/TableRowOperations.pbip](table-row-operations/TableRowOperations.pbip) |
| Table.Table construction | [table-table-construction/TableTableConstruction.pbip](table-table-construction/TableTableConstruction.pbip) |
| Table.Transformation | [table-transformation/TableTransformation.pbip](table-transformation/TableTransformation.pbip) |
| Text | [text/Text.pbip](text/Text.pbip) |
| Text.Conversions from and to text | [text-conversions-from-and-to-text/TextConversionsFromAndToText.pbip](text-conversions-from-and-to-text/TextConversionsFromAndToText.pbip) |
| Text.Extraction | [text-extraction/TextExtraction.pbip](text-extraction/TextExtraction.pbip) |
| Text.Information | [text-information/TextInformation.pbip](text-information/TextInformation.pbip) |
| Text.Membership | [text-membership/TextMembership.pbip](text-membership/TextMembership.pbip) |
| Text.Modification | [text-modification/TextModification.pbip](text-modification/TextModification.pbip) |
| Text.Transformations | [text-transformations/TextTransformations.pbip](text-transformations/TextTransformations.pbip) |
| Type | [type/Type.pbip](type/Type.pbip) |
| Values.Implementation | [values-implementation/ValuesImplementation.pbip](values-implementation/ValuesImplementation.pbip) |

## How to review

1. Open the `.pbip` in Power BI Desktop and click **Refresh**.
2. The **Examples** page lists every block: the function, the code, **Recorded** (the result its
   page shows) and **Live** (what your Power BI returns now). **Match** is `yes` when they agree.
   Filter by function with the slicer on the left.
3. A `NO` in Match means the page and the engine disagree: rerun
   `python lab/runner/run_examples.py --port <port> --write` and read the diff.

The last page, **Thank You!!**, is the author's page (`thank-you/`, copied from the Deneb labs).

## How it works

Refresh evaluates every block the way `lab/runner/` does - `runner.pq` renders each value,
over only the members of `#shared` that `m_blocks.allowed_names` allows. No data source: the
examples compute on literals, so the projects need no credentials and read nothing.

```bash
python lab/review/build_review.py --only number-   # add or rebuild a batch
python lab/review/build_review.py                  # rebuild every batch in this folder
python lab/review/build_review.py --check          # CI: exit 1 if a batch is out of date
```
