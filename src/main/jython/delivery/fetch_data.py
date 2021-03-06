from delivery.ConflictsProcessor import ConflictsProcessor
from delivery.Conflicts import Conflicts

conflicts_processor = ConflictsProcessor(releaseApi)
result_conflicts = Conflicts(releaseApi)
conflicts_processor.analyse(result_conflicts)
result_conflicts.analyze_conflicts()

response.entity = result_conflicts.to_dict()
