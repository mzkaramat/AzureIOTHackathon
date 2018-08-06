# Interface definition for H2O Driverless AI Scoring Service

namespace c_glib H2OAIScoring
namespace cocoa H2OAIScoring
namespace cpp ai.h2o.scoring
namespace csharp Ai.H2O.Scoring
namespace d h2oai_scoring
namespace dart h2oaiscoring
namespace delphi H2OAI.Scoring
namespace go h2oaiscoring
namespace haxe h2oaiscoring
namespace java ai.h2o.scoring
namespace js H2OAIScoring
namespace lua H2OAIScoring
namespace netcore Ai.H2O.Scoring
namespace perl H2OAIScoring
namespace php H2OAIScoring
namespace py h2oai_scoring
namespace rb H2OAIScoring
namespace st H2OAIScoring

const string VERSION = "1.0.0"
const string HASH = "h2oai_experiment_dovudusu"


/** An input row to be scored.
 * @param l3S30D3521, L3_S30_D3521
 */
struct Row {
    1: optional double l3S30D3521,
}

/**
 * Scoring Service
 */
service ScoringService {
    /**
     * Score a single row.
     */
    list<double> score(1:required Row row, 2:optional bool output_margin = false, 3:optional bool pred_contribs = false)

    /**
     * Score multiple rows.
     */
    list<list<double>> score_batch(1:required list<Row> rows, 2:optional bool output_margin = false, 3:optional bool pred_contribs = false)

    /**
     * Fetch an ordered list of labels for the target (response) column.
     * Note that this list will be non-empty only for classification models.
     */
    list<string> get_target_labels()

    /**
     * Fetch the scoring server's model identifier.
     */
    string get_hash()

   /**
    * Fetch the input column names.
   */
   list<string> get_column_names()

   /**
    * Fetch the transformed column names.
   */
   list<string> get_transformed_column_names()
}
