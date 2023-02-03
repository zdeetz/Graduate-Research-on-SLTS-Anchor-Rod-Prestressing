clc,clear,close all
for i = 1:6
    % load data
    data = readtable(['2019_0',num2str(i),'.xlsx']);
    data = table2cell(data);
    date = data(:,1);
    date = string(date);
    data = cell2mat(data(:,2:11));
    % get the starting and end date
    start = date(1); 
    start = extractBetween(start,9,10);
    start = double(start)
    
    enddate = date(end); 
    enddate = extractBetween(enddate,9,10);
    enddate = double(enddate)
    
    h=figure; 
    set(h,'Units','Normalized','Position',[0.05 0.05 0.512 0.35],'Color',[1 1 1])
    subplot(2,1,1);hold on
    h1=plot(start:enddate,data(:,1:2), 'LineWidth', 2);
    legend(h1(1:2),{'Bolt2','Bolt3'})
    hs1=scatter(start:enddate,data(:,1));
    hs2=scatter(start:enddate,data(:,2));
    set(get(get(hs1,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
    set(get(get(hs2,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');

    xlim([1,31])
    grid on
    grid minor
    xlabel('Days','FontSize',12);
    ylabel('Stress range (MPa)','FontName','Times New Roman','FontSize',12);
    title('Equivalent Stress Range (no adjusting)')
    set(gca,'FontName','Times New Roman','fontsize',12);

    subplot(2,1,2);hold on
    h2=plot(start:enddate,data(:,6:7), 'LineWidth', 2);
    legend(h2(1:2),{'Bolt2','Bolt3'})
    hs3=scatter(start:enddate,data(:,6));
    hs4=scatter(start:enddate,data(:,7));
    set(get(get(hs3,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
    set(get(get(hs4,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');

    xlim([1,31])
    grid on
    grid minor
    xlabel('Days','FontSize',12);
    ylabel('Stress range (MPa)','FontName','Times New Roman','FontSize',12);
    title('Equivalent Stress Range (adjusted)')
    set(gca,'FontName','Times New Roman','fontsize',12);
    suptitle(['Year: 2019, Month: ',num2str(i)])
    set(gca,'FontName','Times New Roman','fontsize',12);
end